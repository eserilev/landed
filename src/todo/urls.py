from .views import *
from django.conf.urls import url

app_name = 'todo'
urlpatterns = [
    url(r'^$', ToDoCreateView.as_view(), name='todo_create'),
    url(r'^(?P<cid>\d+)/$', ToDoListView.as_view(), name='todo_list'),
    ]