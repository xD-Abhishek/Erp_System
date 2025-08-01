from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/form.html', {'form': form})

def ticket_edit(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('ticket_list')
    return render(request, 'tickets/form.html', {'form': form})

def ticket_delete(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.delete()
    return redirect('ticket_list')
