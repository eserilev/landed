from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.


class TodoItemModelAdmin(admin.ModelAdmin):
    form = ToDoItemModelForm

class ToDoListModelAdmin(admin.ModelAdmin):
    form = ToDoListModelForm

admin.site.register(ToDoItem, TodoItemModelAdmin)
admin.site.register(ToDoList, ToDoListModelAdmin)