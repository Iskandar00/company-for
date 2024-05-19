from apps.general.models import General


def general(request):

    general_details = General.objects.last()
    print(general_details)
    return {
        'general_details': general_details
    }

