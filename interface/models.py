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
    agent_group_name = models.CharField(max_length=100)  # Название группы агентов
    agent_group_priority = models.IntegerField(blank=True, null=True)  # Приоритет группы агентов
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения
    agent_group_description = models.CharField(max_length=250, blank=True, null=True)  # Описание группы агентов

    class Meta:
        managed = False
        db_table = 't_agent_groups'


# Типы агентов
class AgentTypes(models.Model):
    agent_type = models.CharField(max_length=100)  # Тип агента
    agent_type_description = models.CharField(max_length=250, blank=True, null=True)  # Описание типа агента

    class Meta:
        managed = False
        db_table = 't_agent_types'


# Агенты
class Agents(models.Model):
    agent_name = models.CharField(max_length=250, blank=True, null=True)  # Имя агента
    agent_group = models.ForeignKey(AgentGroups, models.DO_NOTHING, blank=True, null=True)  # Группа агента
    agent_status = models.IntegerField(blank=True, null=True)  # Статус агента
    agent_description = models.CharField(max_length=500, blank=True, null=True)  # Описание агента
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения
    agent_type = models.ForeignKey(AgentTypes, models.DO_NOTHING, blank=True, null=True)  # Тип агента
    agent_mac_address = models.CharField(max_length=250, blank=True, null=True)  # MAC-адрес агента
    agent_ip_address = models.CharField(max_length=250, blank=True, null=True)  # IP-адрес агента
    agent_port = models.CharField(max_length=250, blank=True, null=True)  # Порт агента

    class Meta:
        managed = False
        db_table = 't_agents'


# Файлы агентов
class AgentFiles(models.Model):
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)  # Агент, связанный с файлом
    file_name = models.CharField(max_length=250, blank=True, null=True)  # Имя файла
    file_type = models.CharField(max_length=250, blank=True, null=True)  # Тип файла
    file_path = models.CharField(max_length=250, blank=True, null=True)  # Путь к файлу
    file_description = models.CharField(max_length=250, blank=True, null=True)  # Описание файла
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения

    class Meta:
        managed = False
        db_table = 't_agent_files'


# Состояние нейросети агентов
class AgentNeuralNetworkState(models.Model):
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)  # Агент, связанный с состоянием нейросети
    neural_network_state = models.CharField(max_length=1000000, blank=True, null=True)  # Состояние нейросети агента
    neural_network_state_description = models.CharField(max_length=250, blank=True, null=True)  # Описание состояния нейросети
    create_datetime = models.DateTimeField(blank=True, null=True)  # Дата и время создания

    class Meta:
        managed = False
        db_table = 't_agent_neural_network_state'


# Алгоритмы
class NeuralAlgorithms(models.Model):
    algorithm_name = models.CharField(max_length=250, blank=True, null=True)  # Название алгоритма
    algorithm_code_name = models.CharField(max_length=250, blank=True, null=True)  # Кодовое имя алгоритма
    algorithm_description = models.CharField(max_length=250, blank=True, null=True)  # Описание алгоритма
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения

    class Meta:
        managed = False
        db_table = 't_neural_algorithms'


# Ошибки агентов
class AgentErrors(models.Model):
    agent_step = models.IntegerField(blank=True, null=True)  # Шаг агента
    agent_error_value = models.FloatField(blank=True, null=True)  # Значение ошибки агента
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    agent_error_info = models.CharField(max_length=250, blank=True, null=True)  # Информация об ошибке агента
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)  # Агент, связанный с ошибкой
    algorithm = models.ForeignKey(NeuralAlgorithms, models.DO_NOTHING, blank=True, null=True)  # Алгоритм, связанный с ошибкой

    class Meta:
        managed = False
        db_table = 't_agent_errors'


# Представления базы данных
# Представление агентов
class AgentsView(models.Model):
    id = models.IntegerField(primary_key=True)  # Идентификатор агента
    agent_name = models.CharField(max_length=250, blank=True, null=True)  # Имя агента
    agent_group_name = models.CharField(max_length=100)  # Название группы агента
    agent_group_id = models.IntegerField()  # Идентификатор группы агента
    agent_status = models.CharField(max_length=100)  # Статус агента
    agent_status_id = models.IntegerField()  # Идентификатор статуса агента
    agent_description = models.CharField(max_length=250, blank=True, null=True)  # Описание агента
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения
    agent_type = models.CharField(max_length=100)  # Тип агента
    agent_type_id = models.IntegerField()  # Идентификатор типа агента
    agent_mac_address = models.CharField(max_length=250, blank=True, null=True)  # MAC-адрес агента
    agent_ip_address = models.CharField(max_length=250, blank=True, null=True)  # IP-адрес агента
    agent_ip_address_port = models.CharField(max_length=250, blank=True, null=True)  # IP-адрес и порт агента
    agent_port = models.CharField(max_length=250, blank=True, null=True)  # Порт агента

    class Meta:
        managed = False
        db_table = 'v_agents'


# Представление ошибок агентов
class AgentErrorsView(models.Model):
    id = models.IntegerField(primary_key=True)  # Идентификатор ошибки агента
    agent_step = models.IntegerField(blank=True, null=True)  # Шаг агента
    agent_error_value = models.FloatField(blank=True, null=True)  # Значение ошибки агента
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    agent_error_info = models.CharField(max_length=250, blank=True, null=True)  # Информация об ошибке агента
    agent_name = models.CharField(max_length=250, blank=True, null=True)  # Имя агента
    agent_id = models.IntegerField(blank=True, null=True)  # Идентификатор агента
    algorithm_id = models.IntegerField(blank=True, null=True)  # Идентификатор алгоритма
    algorithm_name = models.CharField(max_length=250, blank=True, null=True)  # Название алгоритма
    algorithm_code_name = models.CharField(max_length=250, blank=True, null=True)  # Кодовое имя алгоритма
    algorithm_description = models.CharField(max_length=250, blank=True, null=True)  # Описание алгоритма


    class Meta:
        managed = False
        db_table = 'v_agent_errors'


# Представление файлов агентов
class AgentFilesView(models.Model):
    id = models.IntegerField(primary_key=True)  # Идентификатор файла
    agent_name = models.CharField(max_length=100)  # Имя агента
    file_name = models.CharField(max_length=250, blank=True, null=True)  # Имя файла
    file_type = models.CharField(max_length=250, blank=True, null=True)  # Тип файла
    file_path = models.CharField(max_length=250, blank=True, null=True)  # Путь к файлу
    file_description = models.CharField(max_length=250, blank=True, null=True)  # Описание файла
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения

    class Meta:
        managed = False
        db_table = 'v_agent_files'


# Представление групп агентов
class AgentGroupsView(models.Model):
    agent_group_name = models.CharField(max_length=100)  # Название группы агентов
    agent_group_priority = models.IntegerField()  # Приоритет группы агентов
    datetime_create = models.DateTimeField()  # Дата и время создания
    datetime_change = models.DateTimeField()  # Дата и время последнего изменения
    agent_group_description = models.CharField(max_length=250, blank=True, null=True)  # Описание группы агентов

    class Meta:
        managed = False
        db_table = 'v_agent_groups'


# Представление типов агентов
class AgentTypesView(models.Model):
    agent_type = models.CharField(max_length=100)  # Тип агента
    agent_type_description = models.CharField(max_length=250, blank=True, null=True)  # Описание типа агента

    class Meta:
        managed = False
        db_table = 'v_agent_types'


# Представления нейросетевого состояния агентов
class AgentNeuralNetworkStateView(models.Model):
    id = models.IntegerField(primary_key=True)  # Идентификатор состояния нейросети
    count_neural_network_state = models.IntegerField()  # Количество состояний нейросети
    neural_network_state_description = models.CharField(max_length=250, blank=True, null=True)  # Описание состояния нейросети
    datetime_create = models.DateTimeField(blank=True, null=True)  # Дата и время создания
    datetime_change = models.DateTimeField(blank=True, null=True)  # Дата и время последнего изменения
    agent_name = models.CharField(max_length=250, blank=True, null=True)  # Имя агента
    agent_group_name = models.CharField(max_length=100)  # Название группы агента
    agent_group_id = models.IntegerField()  # Идентификатор группы агента
    agent_status = models.CharField(max_length=100)  # Статус агента
    agent_status_id = models.IntegerField()  # Идентификатор статуса агента
    agent_description = models.CharField(max_length=250, blank=True, null=True)  # Описание агента
    agent_type = models.CharField(max_length=100)  # Тип агента
    agent_type_id = models.IntegerField()  # Идентификатор типа агента
    agent_mac_address = models.CharField(max_length=250, blank=True, null=True)  # MAC-адрес агента
    agent_ip_address = models.CharField(max_length=250, blank=True, null=True)  # IP-адрес агента
    agent_port = models.CharField(max_length=250, blank=True, null=True)  # Порт агента

    class Meta:
        managed = False
        db_table = 'v_agent_neural_network_state'







