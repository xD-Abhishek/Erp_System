from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    issue = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.lead.name} - {self.status}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title
