# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import VetSerializer
from .models import Vet

# Create your views here.
class VetView(viewsets.ModelViewSet):
    serializer_class = VetSerializer
    queryset = Vet.objects.all()