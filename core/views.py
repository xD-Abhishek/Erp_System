from django.shortcuts import render
from .models import Lead, Ticket, Employee, Task

def home(request):
    context = {
        'lead_count': Lead.objects.count(),
        'ticket_count': Ticket.objects.count(),
        'employee_count': Employee.objects.count(),
        'task_count': Task.objects.count(),
    }
    return render(request, 'core/home.html', context)
