from django.urls import path
from apps.contacts.views import contacts_create, contacts_page

urlpatterns = [
    path('contacts_create', contacts_create, name='contacts_create-page'),
    path('', contacts_page, name='contacts-page')
]
