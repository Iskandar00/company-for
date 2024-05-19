from django.shortcuts import render

from apps.about.models import AboutCompany, CustomerOpinion
from apps.general.models import Workflow, MainView


def home(request):
    customer_opinions = CustomerOpinion.objects.all()
    about_company = AboutCompany.objects.all()
    workflows = Workflow.objects.all()
    main_views = MainView.objects.all()
    context = {
        'customer_opinions': customer_opinions,
        'about_company': about_company,
        'workflows': workflows,
        'main_views': main_views
    }

    return render(request, 'index.html', context)
