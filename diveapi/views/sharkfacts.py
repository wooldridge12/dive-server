"""View module for handling requests about helpsectionposts"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from diveapi.models import SharkFact

class SharkFactsView(ViewSet):
    """Dive Shark facts list"""
    
    def list(self, request):