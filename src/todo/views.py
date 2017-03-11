from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

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

class ToDoDetailView( LoginRequiredMixin, DetailView):
    template_name = 'todo/todo_detail.html'
    queryset = ToDoItem.objects.all()
    pk_url_kwarg = 'tid'

class ToDoMarkCompleteView(LoginRequiredMixin, UpdateView):
    queryset = ToDoItem.objects.all()
    #form_class = ToDoItemModelForm


'''
def ToDo_list_and_update(request):
    form = ToDoListModelForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    objects = ToDoList.objects.all()
    return render(request, 'todo/todo_list.html', {'objects': objects, 'form': form})
'''