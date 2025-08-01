from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    source = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
