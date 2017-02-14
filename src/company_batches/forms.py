from django import forms

from .models import *

class JobTypeModelForm(forms.ModelForm):
    class Meta:
        model = JobType
        fields = [
            "job_title",
            "desired_salary",
            "remote_option",
        ]

class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "city",
            "state",
            "zip",
        ]

class CompanyBatchModelForm(forms.ModelForm):
    class Meta:
        model = CompanyBatch
        fields = [
            "user",
            "company",
            "job_type",
        ]