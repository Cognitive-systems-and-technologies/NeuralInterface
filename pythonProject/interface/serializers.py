# Сериализатор. Обработка данных перед отправкой пользователю
from rest_framework import serializers
from .models import Agents, AgentGroups, AgentTypes, AgentErrorsView


# Сериализатор для получения информации, отображаемой графиком
class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentErrorsView
        fields = ('id', 'agent_step', 'agent_error_value', 'agent_name')