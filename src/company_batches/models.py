from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    name = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip = models.IntegerField()

    def __str__(self):
        return str(self.name)

class JobType(models.Model):
    job_title = models.TextField()
    desired_salary = models.IntegerField()
    remote_option = models.BooleanField()

    def __str__(self):
        return str(self.job_title)

class CompanyBatch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
