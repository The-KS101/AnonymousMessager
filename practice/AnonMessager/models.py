import datetime
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    userMessage = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messageForYou')
    messages = models.TextField(max_length=250)
    pub_date = models.DateTimeField(auto_now=True)

