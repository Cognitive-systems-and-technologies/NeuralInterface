# Представления. Формирование шаблонов и данных для серверного рендеринга
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from .models import AgentsView, AgentGroupsView, AgentTypesView, AgentErrorsView, AgentFilesView
from .models import Agents, AgentGroups, AgentTypes, AgentErrors, AgentFiles, AgentNeuralNetworkState
from .serializers import GraphSerializer, AgentAddSerializer
from django.views.generic import ListView


# Формирование шаблона и данных для серверного рендеринга базовой страницы
def index(request):
    template = loader.get_template('interface/index.html')
    agents = AgentsView.objects.all()
    agentGroups = AgentGroupsView.objects.all()
    agentTypes = AgentTypesView.objects.all()
    agentFiles = AgentFilesView.objects.all()
    agentNeuralNetworkState = AgentNeuralNetworkState.objects.all()
    array = {'agents': agents, 'agentGroups': agentGroups, 'agentTypes': agentTypes,
             'agentFiles': agentFiles, 'agentNeuralNetworkState': agentNeuralNetworkState}
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
            agent_group_id = request.data.get('agent_group_id')
            agent_type_id = request.data.get('agent_type_id')

            try:
                agent_group = AgentGroups.objects.get(id=agent_group_id)
            except AgentGroups.DoesNotExist:
                return Response({"agent_group_id": "Invalid agent group ID"}, status=400)

            try:
                agent_type = AgentTypes.objects.get(id=agent_type_id)
            except AgentTypes.DoesNotExist:
                return Response({"agent_type_id": "Invalid agent type ID"}, status=400)

            # Assign the related objects to the serializer's data
            serializer.validated_data['agent_group'] = agent_group
            serializer.validated_data['agent_type'] = agent_type

            # Save the serializer
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

