#consumers.py
import os
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

from chat import settings


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(self.roomGroupName, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.roomGroupName, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Encrypt the message using the recipient's public key
        recipient_public_key_path = os.path.join(settings.PRIVATE_KEY_DIR, f"{username}_public_key.pem")
        with open(recipient_public_key_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(key_file.read())

        encrypted_message = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": encrypted_message.hex(),  # Send as hex string
                "username": username,
            }
        )

    async def sendMessage(self, event):
        encrypted_message_hex = event["message"]
        username = event["username"]

        # Decrypt message using the recipient's private key
        private_key_path = os.path.join(settings.PRIVATE_KEY_DIR, f"{username}_private_key.pem")
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(key_file.read(), password=None)

        encrypted_message = bytes.fromhex(encrypted_message_hex)
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        await self.send(text_data=json.dumps({"message": decrypted_message.decode(), "username": username}))