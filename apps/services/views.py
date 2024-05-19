from django.shortcuts import render

from apps.services.models import ServiceType


def services(request):
    service_types = ServiceType.objects.all().order_by('-id')

    context = {
        'service_types': service_types
    }

    return render(request, 'services.html', context)
