from .views import *
from django.conf.urls import url

app_name = 'todo'
urlpatterns = [
    url(r'^$', ToDoCreateView.as_view(), name='create'),
    url(r'^(?P<cid>\d+)/$', ToDoListView.as_view(), name='list'),
    url(r'^(?P<cid>\d+)/(?P<tid>\d+)/$', ToDoDetailView.as_view(), name='detail'),
    ]