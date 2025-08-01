from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps the root URL
    path('lead/', include('lead.urls')),  # If you have lead app
]
