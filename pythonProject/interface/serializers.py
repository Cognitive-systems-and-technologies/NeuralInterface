# Сериализатор. Обработка данных перед отправкой пользователю
from rest_framework import serializers
from .models import Agents, AgentGroups, AgentTypes, AgentErrorsView


# Сериализатор для получения информации, отображаемой графиком
class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentErrorsView
        fields = ('id', 'agent_step', 'agent_error_value', 'agent_name', 'agent_error_info')


# Сериализатор для получения информации, отображаемой графиком
class AgentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = ('agent_name', 'agent_group_id', 'agent_status', 'agent_description', 'datetime_create',
                  'agent_type_id', 'agent_mac_address')
