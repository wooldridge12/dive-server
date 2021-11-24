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
        
        facts = SharkFact.objects.all()
        
        serializer = SharkFactSerializer(
            facts, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        "Handle GEt requests for a single shark_fact"
        try:
            shark_fact = SharkFact.objects.get(pk=pk)
            serializer = SharkFactSerializer(shark_fact, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
class SharkFactSerializer(serializers.ModelSerializer):
    """JSON serializer for sharkFacts"""
    
    class Meta:
        """"""
        model = SharkFact
        fields = ('id', 'shark_fact_title', 'shark_fact')