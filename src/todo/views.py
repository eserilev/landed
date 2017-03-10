from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

# Create your views here.
class ToDoListView(ListView,):
    template_name = 'todo/todo_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ToDoListView, self).get_context_data(*args, **kwargs)
        return context
    def get_queryset(self, *args, **kwargs):
        cid = self.kwargs['cid']
        return ToDoList.objects.filter(company__company_id= cid)

class ToDoCreateView( LoginRequiredMixin, CreateView):
    form_class = ToDoItem
    template_name = 'todo/todo_create.html'
    success_url = '/todo/'