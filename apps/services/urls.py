from django.urls import path
from apps.services.views import services

urlpatterns = [
    path('', services, name='services-page')
]
