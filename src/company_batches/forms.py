from django import forms
from django.conf.urls import url, include
from betterforms.multiform import MultiModelForm



from .models import *

class JobModelForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "job_title",
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
            "job",
            "resume",
            "cover_letter"
        ]
        widgets = {
            'company': forms.TextInput,
            'job' : forms.TextInput,
        }

class ResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            "file",
        ]

class CoverLetterModelForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = [
            "file",
        ]