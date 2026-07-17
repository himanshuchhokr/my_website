from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'tag', 'status', 'commit_hash', 'created_at', 'updated_at']
        read_only_fields = ['id', 'commit_hash', 'created_at', 'updated_at']
