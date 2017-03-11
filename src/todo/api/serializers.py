from rest_framework import serializers

from src.accounts.api.serializers import UserDisplaySerializer
from ..models import *


class ToDoItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = [
            'title',
            'description',
            'rank'
        ]

class ToDoListModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    todo_item = ToDoItemModelSerializer()
    class Meta:
        model = ToDoList
        fields = [
            'user',
            'todo_item',
            'is_complete',

        ]

