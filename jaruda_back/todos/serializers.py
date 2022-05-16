from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' 


class CreateTodoSerializer(serializers.ModelSerializer):
    task = serializers.CharField(max_length=100, help_text="할일", default="수공~")

    class Meta:
        model = Todo
        fields = ['id', 'task', 'create_at']


class EditTodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    task = serializers.CharField(max_length=100, help_text="할일", default="수공~")

    class Meta:
        model = Todo
        fields = ['id', 'task']


    