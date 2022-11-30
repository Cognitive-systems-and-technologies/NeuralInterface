from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from .models import Agents, AgentGroups, AgentTypes, AgentCoordinates
from django.views.generic import ListView


# def agents(request):
#     return render(request, 'interface/index.html', {'agents': Agents.objects.all()})


def index(request):
    template = loader.get_template('interface/index.html')
    agents = Agents.objects.all()
    agentGroups = AgentGroups.objects.all()
    agentTypes = AgentTypes.objects.all()
    agentCoordinates = AgentCoordinates.objects.all()
    array = {'agents': agents, 'agentGroups': agentGroups, 'agentTypes': agentTypes,
             'agentCoordinates': agentCoordinates}
    return HttpResponse(template.render(array, request))


def monitor(request):
    template = loader.get_template('interface/monitor.html')
    agents = Agents.objects.all()
    agentGroups = AgentGroups.objects.all()
    agentTypes = AgentTypes.objects.all()
    agentCoordinates = AgentCoordinates.objects.all()
    array = {'agents': agents, 'agentGroups': agentGroups, 'agentTypes': agentTypes,
             'agentCoordinates': agentCoordinates}
    return HttpResponse(template.render(array, request))

# class interfaceAPIView(generics.ListAPIView):
#     def get(self, request):
#         lst = Files.objects.all().values()
#         return Response({'post': list(lst)})

# class interfaceAPIView(generics.ListAPIView):
#    queryset = Files.objects.all()
#     serializer_class = FilesSerializer
