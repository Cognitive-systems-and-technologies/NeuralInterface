# Модель. Описание таблиц БД
from django.db import models
from django.db.models.fields import related


# Описание таблицы типов агентов
class AgentTypes(models.Model):
    agent_type = models.CharField(max_length=100)

    def __str__(self):
        return self.agent_type


# Описание таблицы групп агентов
class AgentGroups(models.Model):
    agent_group_name = models.CharField(max_length=100)
    agent_group_priority = models.IntegerField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_group_name


# Описание таблицы данных агентов
class Agents(models.Model):
    agent_port = models.IntegerField()
    agent_name = models.CharField(max_length=100)
    agent_status = models.IntegerField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_change = models.DateTimeField(auto_now_add=True)
    agent_type = models.ForeignKey(AgentTypes, on_delete=models.CASCADE)
    agent_group = models.ForeignKey(AgentGroups, on_delete=models.CASCADE)

    def __str__(self):
        return self.agent_name


# Описание таблицы ошибок агентов
class AgentErrors(models.Model):
    agent_step = models.IntegerField()
    agent_error_value = models.FloatField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    agent_port = models.ForeignKey(Agents, on_delete=models.CASCADE)

    def __int__(self):
        return self.agent_error_value

