from django.db import models

# Create your models here.
from django.db.models.fields import related


class Files(models.Model):
    id_file = models.IntegerField()
    name = models.CharField(max_length=100)
    path_file = models.TextField(max_length=300, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    id_file_foreign = models.ForeignKey('FilesLogs', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class FilesLogs(models.Model):
    id_file = models.IntegerField()
    time_update = models.DateTimeField(auto_now=True)
    check_status = models.BooleanField()

    def __int__(self):
        return self.id_file



