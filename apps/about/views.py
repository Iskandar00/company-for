from django.shortcuts import render
from apps.about.models import AboutCompany, Workers, CustomerOpinion


def about(request):
    about_company = AboutCompany.objects.all()
    workers = Workers.objects.all()
    customer_opinions = CustomerOpinion.objects.all()

    context = {
        'about_company': about_company,
        'workers': workers,
        'customer_opinions': customer_opinions
    }
    return render(request, 'about.html', context)
