from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .mixins import FormUserNeededMixin
# Create your views here.

class CompanyBatchCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
    form_class = CompanyBatchModelForm
    template_name = 'company_batches/companybatch_create.html'
    success_url = '/batches/'

class CompanyCreateView(FormUserNeededMixin,CreateView):
    form_class = CompanyModelForm
    template_name = 'company_batches/company_create_view.html'
    success_url = '/batches/'

class JobCreateView(FormUserNeededMixin,CreateView):
    form_class = JobModelForm
    template_name = 'company_batches/job_create_view.html'
    success_url = '/batches/'

class ResumeCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
    form_class = ResumeModelForm
    template_name = 'company_batches/resume_create.html'
    success_url = '/batches/'

class CoverLetterCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
    form_class = CoverLetterModelForm
    template_name = 'company_batches/cv_create.html'
    success_url = '/batches/'
#class ResumeCreateView(FormUserNeededMixin,CreateView):


class CompanyBatchListView(ListView):
    queryset = CompanyBatch.objects.all()
    template_name = 'company_batches/companybatch_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyBatchListView, self).get_context_data(*args, **kwargs)
        return context