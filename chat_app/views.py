import json
from django.shortcuts import render, redirect
import rsa
from django.http import JsonResponse
from .models import UserKey


def chat(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat_app/chat.html", context)

def create_user_key(username):
    # Generate RSA keys
    public_key, private_key = rsa.newkeys(512)

    # Save the public key
    UserKey.objects.create(
        username=username,
        public_key=public_key.save_pkcs1()
    )

    # Private key could be saved securely or provided only to the user
    return private_key.save_pkcs1()

def get_public_key(request):
    username = request.GET.get('username')
    user_key = UserKey.objects.get(username=username)
    return JsonResponse({'public_key': user_key.public_key.decode('utf-8')})

def decrypt_message(encrypted_message, private_key_str):
    private_key = rsa.PrivateKey.load_pkcs1(private_key_str)
    return rsa.decrypt(encrypted_message, private_key).decode('utf-8')

async def receive(self, text_data):
    data = json.loads(text_data)
    encrypted_message = data["message"]

    # Get recipient's private key
    recipient_key = UserKey.objects.get(username=data['recipient'])
    private_key = recipient_key.private_key  # Load or retrieve private key securely

    decrypted_message = decrypt_message(encrypted_message.encode('utf-8'), private_key)