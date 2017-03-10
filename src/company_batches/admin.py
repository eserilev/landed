from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class CompanyBatchModelAdmin(admin.ModelAdmin):
    form = CompanyBatchModelForm

class CompanyModelAdmin(admin.ModelAdmin):
    form = CompanyModelForm

class JobModelAdmin(admin.ModelAdmin):
    form = JobModelForm

class ResumeModelAdmin(admin.ModelAdmin):
    form = ResumeModelForm

class CoverLetterModelAdmin(admin.ModelAdmin):
    form = CoverLetterModelForm

admin.site.register(CompanyBatch, CompanyBatchModelAdmin)
admin.site.register(Company, CompanyModelAdmin)
admin.site.register(Job, JobModelAdmin)
admin.site.register(Resume, ResumeModelAdmin)
admin.site.register(CoverLetter, CoverLetterModelAdmin)