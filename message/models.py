from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    message = models.TextField()
