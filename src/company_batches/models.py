from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
fr = FileSystemStorage(location='batches/job/resume')
fc = FileSystemStorage(location ='batches/job/cover')

# Create your models here.


class Resume(models.Model):
    file = models.FileField(storage=fr, blank=True)

    def __str__(self):
        return os.path.basename(self.file.name)


class CoverLetter(models.Model):
    file = models.FileField(storage=fc, blank=True)

    def __str__(self):
        return os.path.basename(self.file.name)


class Job(models.Model):
    job_title = models.TextField(unique=True)
    avg_salary = models.IntegerField()

    def __str__(self):
        return str(self.job_title)


class Company(models.Model):
    name = models.TextField(unique=True)
    city = models.TextField()
    state = models.TextField()
    zip = models.IntegerField()

    def __str__(self):
        return str(self.name)


class CompanyBatch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.ForeignKey(Company)
    job = models.ForeignKey(Job)
    resume = models.ForeignKey(Resume, null=True)
    cover_letter = models.ForeignKey(CoverLetter, null=True)

    def __str__(self):
        return str(self.company)