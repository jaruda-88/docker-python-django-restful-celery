from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__' 
        fields = ['id', 'task', 'create_at']
    task = serializers.CharField(max_length=100)


    