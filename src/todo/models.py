from django.db import models
from django.conf import settings
from django.core import validators


alpha_c = validators.RegexValidator(r'^[A-C]*$', 'Only ranks A-C are allowed.')
# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    rank = models.CharField(max_length=1, validators=[alpha_c])

    def __str__(self):
        return str(self.title)

class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    todo_item = models.ForeignKey(ToDoItem)
    company = models.ForeignKey('company_batches.CompanyBatch')
    is_complete = models.BooleanField()

    def __str__(self):
        return str(self.todo_item)




