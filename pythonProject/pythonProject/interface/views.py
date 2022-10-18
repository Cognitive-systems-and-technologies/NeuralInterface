from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader

from .models import Files
from .serializers import FilesSerializer


def index(request):
    template = loader.get_template('interface/index.html')
    lst = Files.objects.all().values()
    context = {'post': list(lst)}
    return HttpResponse(template.render(context, request))


class interfaceAPIView(generics.ListAPIView):
    def get(self, request):
        lst = Files.objects.all().values()
        return Response({'post': list(lst)})

# class interfaceAPIView(generics.ListAPIView):
#    queryset = Files.objects.all()
#     serializer_class = FilesSerializer
