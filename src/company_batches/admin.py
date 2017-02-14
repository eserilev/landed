from django.contrib import admin
from .models import CompanyBatch, Company, JobType
from .forms import *
# Register your models here.

class CompanyBatchModelAdmin(admin.ModelAdmin):
    form = CompanyBatchModelForm

class CompanyModelAdmin(admin.ModelAdmin):
    form = CompanyModelForm

class JobTypeModelAdmin(admin.ModelAdmin):
    form = JobTypeModelForm

admin.site.register(CompanyBatch, CompanyBatchModelAdmin)
admin.site.register(Company, CompanyModelAdmin)
admin.site.register(JobType, JobTypeModelAdmin)