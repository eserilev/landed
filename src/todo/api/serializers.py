from rest_framework import serializers

#from ...accounts.api.serializers import UserDisplaySerializer
from ..models import ToDoList

class ToDoListModelSerializer(serializers.ModelSerializer):
    #user = UserDisplaySerializer()
    class Meta:
        model = ToDoList
        fields = [
            'is_complete'
        ]