from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



# Store E2EE keys
class UserKey(models.Model):
    username = models.CharField(max_length=150, unique=True)
    public_key = models.BinaryField()

    def __str__(self):
        return self.username