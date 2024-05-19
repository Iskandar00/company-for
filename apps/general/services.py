from django.utils.translation import get_language


def field_language(self, field_name):
    return getattr(self, f'{field_name}_{get_language()}')
