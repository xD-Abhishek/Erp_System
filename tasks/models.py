from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.CharField(max_length=50)
