from django.contrib import admin
from .models import Lead, Ticket, Employee, Task

admin.site.register(Lead)
admin.site.register(Ticket)
admin.site.register(Employee)
admin.site.register(Task)
