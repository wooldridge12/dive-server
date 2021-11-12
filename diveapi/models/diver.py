from django.db import models
from django.contrib.auth.models import User

class Diver(models.Model):
    """Diver Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    diver = models.CharField(max_length=30)
    