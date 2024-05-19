from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from apps.contacts.forms import ContactForm
from apps.contacts.models import Email, PhoneNumber, Location


def contacts_page(request):
    email = Email.objects.all()
    phone_number = PhoneNumber.objects.all()
    location = Location.objects.all()

    context = {
        'email': email,
        'phone_number': phone_number,
        'location': location
    }

    return render(request, 'contact.html', context)


def contacts_create(request):
    redirect_url = request.META['HTTP_REFERER']
    if request.method != 'POST':
        return render(request, 'contact.html')
    data = request.POST
    form = ContactForm(data=data)
    if form.is_valid():
        form.save()
        messages.success(request, _('the appeal was accepted'))
        return redirect(redirect_url)
    else:
        messages.error(request, form.errors)
        return redirect(redirect_url)

