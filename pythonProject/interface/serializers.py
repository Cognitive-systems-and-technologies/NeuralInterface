# Сериализатор. Обработка данных перед отправкой пользователю
from rest_framework import serializers
from .models import Agents, AgentGroups, AgentTypes, AgentErrorsView


# Сериализаторы для агентов
class AgentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = ('agent_name', 'agent_group_id', 'agent_status', 'agent_description', 'datetime_create',
                  'agent_type_id', 'agent_mac_address', 'agent_ip_address', 'agent_port')


class AgentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'


class AgentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'


# Сериализаторы для групп агентов
class GroupAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentGroups
        fields = ('agent_group_name', 'agent_group_priority', 'datetime_create', 'agent_group_description')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentGroups
        fields = '__all__'


class SyncAgentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = ('agent_name', 'agent_status', 'datetime_create', 'datetime_change',
                  'agent_mac_address', 'agent_ip_address', 'agent_port')


# Сериализатор для получения информации, отображаемой графиком
class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentErrorsView
        fields = ('id', 'agent_step', 'agent_error_value', 'agent_id', 'agent_name', 'agent_error_info')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentErrorsView
        fields = ('id', 'agent_step', 'agent_error_value', 'agent_name', 'agent_error_info')
