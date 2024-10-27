import json
from django.shortcuts import render, redirect
import rsa
from django.http import JsonResponse
import os
import django
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from django.contrib.auth.models import User
from .models import Message

django.setup()

# Directory to store keys
KEYS_DIR = 'keys'

# Ensure the directory exists
os.makedirs(KEYS_DIR, exist_ok=True)

def generate_key_pair(username):
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate public key
    public_key = private_key.public_key()

    # Serialize private key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serialize public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save keys to files
    with open(os.path.join(KEYS_DIR, f'{username}_private_key.pem'), 'wb') as private_file:
        private_file.write(private_pem)
    with open(os.path.join(KEYS_DIR, f'{username}_public_key.pem'), 'wb') as public_file:
        public_file.write(public_pem)

    print(f"Keys generated and saved for {username}")





def chat(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    generate_key_pair(request.user)

    messages = Message.objects.filter(receiver=request.user)
    context = {
        'messages': messages,
    }
    return render(request, "chat_app/chat.html", context)
