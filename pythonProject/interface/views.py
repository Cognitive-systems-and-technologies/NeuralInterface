# Представления. Формирование шаблонов и данных для серверного рендеринга
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from .models import AgentsView, AgentGroupsView, AgentTypesView, AgentErrorsView, AgentFilesView
from .models import Agents, AgentGroups, AgentTypes, AgentErrors, AgentFiles
from .serializers import GraphSerializer, AgentAddSerializer
from django.views.generic import ListView


# Формирование шаблона и данных для серверного рендеринга базовой страницы
def index(request):
    template = loader.get_template('interface/index.html')
    agents = AgentsView.objects.all()
    agentGroups = AgentGroupsView.objects.all()
    agentTypes = AgentTypesView.objects.all()
    AgentFiles = AgentFilesView.objects.all()
    array = {'agents': agents, 'agentGroups': agentGroups, 'agentTypes': agentTypes,
             'agentFiles': AgentFiles}
    return HttpResponse(template.render(array, request))


# Формирование шаблона и данных для серверного рендеринга страницы с графиком
def monitor(request):
    template = loader.get_template('interface/monitor.html')
    agents = AgentsView.objects.all()
    agentErrors = AgentErrorsView.objects.all()
    array = {'agents': agents, 'agentErrors': agentErrors}
    return HttpResponse(template.render(array, request))


# Django REST API. Данные для графика на странице
class GraphApiData(generics.ListAPIView):
    queryset = AgentErrorsView.objects.all()
    serializer_class = GraphSerializer


# Django REST API. Данные для добавления новой записи агента
class AgentAddData(generics.ListAPIView):
    def post(self, request):
        serializer = AgentAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

