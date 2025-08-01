from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadForm

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead/list.html', {'leads': leads})

def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm()
    return render(request, 'lead/add.html', {'form': form})
