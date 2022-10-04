from rest_framework import generics
from django.shortcuts import render
from .models import Files
from .serializers import FilesSerializer


class interfaceAPIView(generics.ListAPIView):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
