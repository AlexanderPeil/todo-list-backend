from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'  
        read_only_fields = ('author',)



    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return TodoItem.objects.create(**validated_data) 