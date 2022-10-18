from rest_framework import serializers
from .models import Files

class FileModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class FilesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

def encode():
    model = FileModel()
