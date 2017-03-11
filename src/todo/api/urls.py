from django.conf.urls import url

from .views import (
    ToDoListAPIView
)
urlpatterns = [
    url(r'^$', ToDoListAPIView.as_view(), name='list')
    ]