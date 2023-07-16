# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Таблицы базы данных
# Группы агентов
class AgentGroups(models.Model):
    agent_group_name = models.CharField(max_length=100)
    agent_group_priority = models.IntegerField(blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)
    agent_group_description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_groups'

# Типы агентов
class AgentTypes(models.Model):
    agent_type = models.CharField(max_length=100)
    agent_type_description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_types'


# Агенты
class Agents(models.Model):
    agent_name = models.CharField(max_length=250, blank=True, null=True)
    agent_group = models.ForeignKey(AgentGroups, models.DO_NOTHING, blank=True, null=True)
    agent_status = models.IntegerField(blank=True, null=True)
    agent_description = models.CharField(max_length=500, blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)
    agent_type = models.ForeignKey(AgentTypes, models.DO_NOTHING, blank=True, null=True)
    agent_mac_address = models.CharField(max_length=250, blank=True, null=True)
    agent_ip_address = models.CharField(max_length=250, blank=True, null=True)
    agent_port = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agents'


# Файлы агентов
class AgentFiles(models.Model):
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    file_name = models.CharField(max_length=250, blank=True, null=True)
    file_type = models.CharField(max_length=250, blank=True, null=True)
    file_path = models.CharField(max_length=250, blank=True, null=True)
    file_description = models.CharField(max_length=250, blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_files'


# Состояние нейросети агентов
class AgentNeuralNetworkState(models.Model):
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    neural_network_state = models.CharField(max_length=1000000, blank=True, null=True)
    neural_network_state_description = models.CharField(max_length=250, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_neural_network_state'


# Алгоритмы
class NeuralAlgorithms(models.Model):
    algorithm_name = models.CharField(max_length=250, blank=True, null=True)
    algorithm_code_name = models.CharField(max_length=250, blank=True, null=True)
    algorithm_description = models.CharField(max_length=250, blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_neural_algorithms'


# Ошибки агентов
class AgentErrors(models.Model):
    agent_step = models.IntegerField(blank=True, null=True)
    agent_error_value = models.FloatField(blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    agent_error_info = models.CharField(max_length=250, blank=True, null=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    algorithm = models.ForeignKey(NeuralAlgorithms, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_errors'


# Представления базы данных
# Представление агентов
class AgentsView(models.Model):
    id = models.IntegerField(primary_key=True)
    agent_name = models.CharField(max_length=250, blank=True, null=True)
    agent_group_name = models.CharField(max_length=100)
    agent_group_id = models.IntegerField()
    agent_status = models.CharField(max_length=100)
    agent_status_id = models.IntegerField()
    agent_description = models.CharField(max_length=250, blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)
    agent_type = models.CharField(max_length=100)
    agent_type_id = models.IntegerField()
    agent_mac_address = models.CharField(max_length=250, blank=True, null=True)
    agent_ip_address = models.CharField(max_length=250, blank=True, null=True)
    agent_ip_address_port = models.CharField(max_length=250, blank=True, null=True)
    agent_port = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_agents'


# Представление ошибок агентов
class AgentErrorsView(models.Model):
    id = models.IntegerField(primary_key=True)
    agent_step = models.IntegerField(blank=True, null=True)
    agent_error_value = models.FloatField(blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    agent_error_info = models.CharField(max_length=250, blank=True, null=True)
    agent_name = models.CharField(max_length=250, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    algorithm_id = models.IntegerField(blank=True, null=True)
    algorithm_name = models.CharField(max_length=250, blank=True, null=True)
    algorithm_code_name = models.CharField(max_length=250, blank=True, null=True)
    algorithm_description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_agent_errors'


# Представление файлов агентов
class AgentFilesView(models.Model):
    id = models.IntegerField(primary_key=True)
    agent_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=250, blank=True, null=True)
    file_type = models.CharField(max_length=250, blank=True, null=True)
    file_path = models.CharField(max_length=250, blank=True, null=True)
    file_description = models.CharField(max_length=250, blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_agent_files'


# Представление групп агентов
class AgentGroupsView(models.Model):
    agent_group_name = models.CharField(max_length=100)
    agent_group_priority = models.IntegerField()
    datetime_create = models.DateTimeField()
    datetime_change = models.DateTimeField()
    agent_group_description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_agent_groups'


# Представление типов агентов
class AgentTypesView(models.Model):
    agent_type = models.CharField(max_length=100)
    agent_type_description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_agent_types'


# Представления нейросетевого состояния агентов
class AgentNeuralNetworkStateView(models.Model):
    id = models.IntegerField(primary_key=True)
    count_neural_network_state = models.IntegerField()
    neural_network_state_description = models.CharField(max_length=250, blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)
    agent_name = models.CharField(max_length=250, blank=True, null=True)
    agent_group_name = models.CharField(max_length=100)
    agent_group_id = models.IntegerField()
    agent_status = models.CharField(max_length=100)
    agent_status_id = models.IntegerField()
    agent_description = models.CharField(max_length=250, blank=True, null=True)
    agent_type = models.CharField(max_length=100)
    agent_type_id = models.IntegerField()
    agent_mac_address = models.CharField(max_length=250, blank=True, null=True)
    agent_ip_address = models.CharField(max_length=250, blank=True, null=True)
    agent_port = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_agent_neural_network_state'







