from django.db import models

# Create your models here.
from django.db.models.fields import related


class AgentTypes(models.Model):
    agent_type = models.CharField(max_length=100)

    def __str__(self):
        return self.agent_type


class AgentGroups(models.Model):
    agent_group_name = models.CharField(max_length=100)
    agent_group_priority = models.IntegerField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_group_name


class Agents(models.Model):
    agent_name = models.CharField(max_length=100)
    agent_status = models.IntegerField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_change = models.DateTimeField(auto_now_add=True)
    agent_type = models.ForeignKey(AgentTypes, on_delete=models.CASCADE)
    agent_group = models.ForeignKey(AgentGroups, on_delete=models.CASCADE)

    def __str__(self):
        return self.agent_name


class AgentCoordinates(models.Model):
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    agent_id = models.ForeignKey(Agents, on_delete=models.CASCADE)

    def __int__(self):
        return self.coordinate_y


# class Test(models.Model):
#     name = models.CharField(max_length=100)
#     path_file = models.TextField(max_length=300, blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name


# class Files(models.Model):
#     id_file = models.IntegerField()
#     name = models.CharField(max_length=100)
#     path_file = models.TextField(max_length=300, blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     id_file_foreign = models.ForeignKey('FilesLogs', on_delete=models.PROTECT, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class FilesLogs(models.Model):
#     id_file = models.IntegerField()
#     time_update = models.DateTimeField(auto_now=True)
#     check_status = models.BooleanField()
#
#     def __int__(self):
#         return self.id_file
