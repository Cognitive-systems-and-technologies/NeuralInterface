# Представления. Формирование шаблонов и данных для серверного рендеринга
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from .models import AgentsView, AgentGroups, AgentTypes, AgentErrorsView, AgentFilesView
from .serializers import GraphSerializer
from django.views.generic import ListView


# Формирование шаблона и данных для серверного рендеринга базовой страницы
def index(request):
    template = loader.get_template('interface/index.html')
    agents = AgentsView.objects.all()
    agentGroups = AgentGroups.objects.all()
    agentTypes = AgentTypes.objects.all()
    AgentFiles = AgentFilesView.objects.all()
    agentCoordinates = AgentErrorsView.objects.all()
    array = {'agents': agents, 'agentGroups': agentGroups, 'agentTypes': agentTypes,
             'agentCoordinates': agentCoordinates, 'agentFiles': AgentFiles}
    return HttpResponse(template.render(array, request))


# Формирование шаблона и данных для серверного рендеринга страницы с графиком
def monitor(request):
    template = loader.get_template('interface/monitor.html')
    agents = AgentsView.objects.all()
    agentGroups = AgentGroups.objects.all()
    agentTypes = AgentTypes.objects.all()
    agentErrors = AgentErrorsView.objects.all()
    array = {'agents': agents, 'agentGroups': agentGroups, 'agentTypes': agentTypes,
             'agentErrors': agentErrors}
    return HttpResponse(template.render(array, request))


# Django REST API. Данные для графика на странице
class graphApiData(generics.ListAPIView):
    queryset = AgentErrorsView.objects.all()
    serializer_class = GraphSerializer

