from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lead/', include('lead.urls')),
    path('tickets/', include('tickets.urls')),
    path('employees/', include('employees.urls')),
    path('tasks/', include('tasks.urls')),
    path('', include('core.urls')),
]
