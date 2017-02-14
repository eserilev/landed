from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import *
from .forms import *
from .mixins import FormUserNeededMixin
# Create your views here.

class CompanyBatchListView(ListView):
    queryset = CompanyBatch.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyBatchListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context