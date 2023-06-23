# Представления. Формирование шаблонов и данных для серверного рендеринга
from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from .models import AgentsView, AgentGroupsView, AgentTypesView, AgentErrorsView, AgentFilesView, \
    AgentNeuralNetworkStateView
from .models import Agents, AgentGroups, AgentTypes, AgentErrors, AgentFiles, AgentNeuralNetworkState
from .serializers import GraphSerializer, AgentAddSerializer, SyncAgentDataSerializer, AgentDeleteSerializer, \
    AgentEditSerializer, GroupAddSerializer, GroupSerializer
from django.views.generic import ListView
import json
from datetime import datetime
import requests
from django.http import JsonResponse
from django.middleware import csrf


# Формирование шаблона и данных для серверного рендеринга базовой страницы
def index(request):
    template = loader.get_template('interface/index.html')
    agents = AgentsView.objects.all()
    agentGroups = AgentGroupsView.objects.all()
    agentTypes = AgentTypesView.objects.all()
    agentFiles = AgentFilesView.objects.all()
    agentNeuralNetworkState = AgentNeuralNetworkStateView.objects.all()
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


# Формирование шаблона и данных для серверного рендеринга страницы с информацией
def info(request):
    template = loader.get_template('interface/info.html')
    agents = AgentsView.objects.all()
    agentErrors = AgentErrorsView.objects.all()
    array = {'agents': agents, 'agentErrors': agentErrors}
    return HttpResponse(template.render(array, request))


# Django REST API. Данные для добавления новой записи агента
class AgentAddData(generics.ListAPIView):
    def post(self, request):
        serializer = AgentAddSerializer(data=request.data)
        if serializer.is_valid():
            agent_group_id = request.data.get('agent_group_id')
            agent_type_id = request.data.get('agent_type_id')
            agent_mac_address = request.data.get('agent_mac_address')
            agent_mac_address_check = Agents.objects.filter(agent_mac_address=agent_mac_address).exists()

            if agent_mac_address_check:
                message = "Агент с таким MAC адрессм уже существует"
                return Response(message, status=status.HTTP_200_OK)

            try:
                agent_group = AgentGroups.objects.get(id=agent_group_id)
            except AgentGroups.DoesNotExist:
                return Response({"agent_group_id": "Invalid agent group ID"}, status=400)

            try:
                agent_type = AgentTypes.objects.get(id=agent_type_id)
            except AgentTypes.DoesNotExist:
                return Response({"agent_type_id": "Invalid agent type ID"}, status=400)

            try:
                agent_mac_address_check = Agents.objects.get(id=agent_type_id)
            except AgentTypes.DoesNotExist:
                return Response({"agent_type_id": "Invalid agent type ID"}, status=400)

            # Assign the related objects to the serializer's data
            serializer.validated_data['agent_group'] = agent_group
            serializer.validated_data['agent_type'] = agent_type

            # Save the serializer
            serializer.save()
            return Response("Агент успешно добавлен", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)


class AgentEditData(generics.UpdateAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentEditSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            agent_group_id = request.data.get('agent_group_id')
            agent_type_id = request.data.get('agent_type_id')
            agent_mac_address = request.data.get('agent_mac_address')
            agent_id = instance.id
            agent = Agents.objects.get(agent_mac_address=agent_mac_address)
            agent_id_db = agent.id
            agent_mac_address_check = Agents.objects.filter(agent_mac_address=agent_mac_address).exists()

            if agent_mac_address_check and agent_id != agent_id_db:
                message = "Агент с таким MAC адрессом уже существует"
                return Response(message, status=status.HTTP_200_OK)

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

            self.perform_update(serializer)
            return Response("Агент успешно изменен", status.HTTP_200_OK)
        return Response(serializer.errors, status=400)


class AgentDeleteData(generics.DestroyAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentDeleteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        agent_id = instance.id
        errors_exist = AgentErrors.objects.filter(agent_id=agent_id).exists()
        neural_state_exist = AgentNeuralNetworkState.objects.filter(agent_id=agent_id).exists()
        errors_file_exist = AgentFiles.objects.filter(agent_id=agent_id).exists()

        if errors_file_exist:
            message = "Запись с привязкой данного агента существует в таблице файлов агентов"
        elif errors_exist:
            message = "Запись с привязкой данного агента существует в таблице обучения агентов"
        elif neural_state_exist:
            message = "Запись с привязкой данного агента существует в таблице состояний нейросети"
        else:
            message = 'Агент успешно удален'
            instance.delete()
            return Response(message, status=status.HTTP_200_OK)

        return Response(message, status=status.HTTP_200_OK)


class GroupAddData(generics.ListAPIView):
    def post(self, request):
        serializer = GroupAddSerializer(data=request.data)
        if serializer.is_valid():
            # Save the serializer
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GroupEditData(generics.UpdateAPIView):
    queryset = AgentGroups.objects.all()
    serializer_class = GroupSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class GroupDeleteData(generics.DestroyAPIView):
    queryset = AgentGroups.objects.all()
    serializer_class = GroupSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        group_id = instance.id
        group_exist = Agents.objects.filter(agent_group_id=group_id).exists()

        if group_exist:
            message = "Запись с привязкой данной группы существует в таблице агентов"
        else:
            message = 'Группа успешно удалена'
            instance.delete()
            return Response(message, status=status.HTTP_200_OK)

        return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
def syncAgentData(request):
    if request.data.get('m') == 'authorization':
        agent_data_json = request.data.get('b')
        agent_data = json.loads(agent_data_json)
        print(agent_data)
        agent_name = agent_data['name']
        agent_ip_address = request.META.get('REMOTE_ADDR')
        agent_mac_address = agent_data['mac']
        agent_port = agent_data['port']
        agent_data_add = {'agent_name': agent_name,
                          'agent_mac_address': agent_mac_address,
                          'agent_ip_address': agent_ip_address,
                          'agent_port': agent_port,
                          'agent_status': '1',
                          'datetime_change': datetime.now(),
                          'datetime_create': datetime.now()
                          }
        serializer = SyncAgentDataSerializer(data=agent_data_add)
        if serializer.is_valid():
            try:
                agent = Agents.objects.get(agent_mac_address=agent_mac_address)
                agent.agent_name = agent_name
                print(agent_name)
                agent.agent_ip_address = agent_ip_address
                agent.agent_port = agent_port
                agent.agent_status = 1
                agent.datetime_change = datetime.now()
                agent.save()
            except Agents.DoesNotExist:
                Agents.objects.create(
                    agent_name=agent_name,
                    agent_mac_address=agent_mac_address,
                    agent_ip_address=agent_ip_address,
                    agent_port=agent_port,
                    agent_status=1,
                    datetime_create=datetime.now()
                )

            return Response({'message': 'Agent info saved/updated successfully.'})
        else:
            return Response(serializer.errors, status=400)


# Django REST API. Данные для графика на странице
class GraphApiData(generics.ListAPIView):
    serializer_class = GraphSerializer

    def get_queryset(self):
        agent_id = self.request.query_params.get('agent_id')
        if agent_id is None:
            return Response("agent_id parameter is required.", status=400)
        return AgentErrorsView.objects.filter(agent_id=agent_id)


class SendRequestDjango(generics.ListAPIView):
    def post(self, request):

        csrf_token = request.META.get('CSRF_COOKIE', '')

        # Set up the request headers
        headers = {
            'X-CSRFToken': csrf_token  # Include the CSRF token in the headers
        }
        print(headers)
        # Send an HTTP request using the extracted data
        response = requests.post('http://127.0.0.1:8000/api/graphData', headers=headers)

        # Process the response
        if response.status_code == 200:
            # Request successful
            return JsonResponse({'success': True})
        else:
            # Request failed
            return JsonResponse({'success': False, 'error': 'Request failed'})
