from rest_framework import serializers
from .models import Files


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('name', 'path_file')
