from rest_framework import generics

from ..models import ToDoList
from .serializers import ToDoListModelSerializer

class ToDoListAPIView(generics.ListAPIView):
    serializer_class = ToDoListModelSerializer

    def get_queryset(self):
        return ToDoList.objects.all()
