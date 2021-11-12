from django.db import models


class SharkFact(models.Model):
    """Shark info model"""
    shark_fact_title = models.CharField(max_length=500)
    shark_fact = models.CharField(max_length=1000)
    