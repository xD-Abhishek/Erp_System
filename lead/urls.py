from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_lead, name='add_lead'),
    path('list/', views.lead_list, name='lead_list'),
]
