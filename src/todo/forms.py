from django import forms
from betterforms.multiform import MultiModelForm

from .models import *

class ToDoItemModelForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            "title",
            "description",
            "rank",
        ]

class ToDoListModelForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = [
            "user",
            "todo_item",
            "company",
            "is_complete",
        ]