from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    role = models.CharField(max_length=20)

class Task(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=10000)
    dateStartAdmin = models.DateField()
    dateFinishAdmin = models.DateField()
    dateStartWorker = models.DateField(null=True)
    dateFinishWorker = models.DateField(null=True)
    status = models.CharField(max_length=20)

class Role(models.Model):
    role = models.CharField(max_length=20)
