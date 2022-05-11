from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' 


class PostTodoSerializer(serializers.ModelSerializer):
    task = serializers.CharField(max_length=100, help_text="할일", default="task")

    class Meta:
        model = Todo
        fields = ['id', 'task', 'create_at']


    