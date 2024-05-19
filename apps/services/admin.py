from django.contrib import admin

from apps.services.models import ServiceType


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'image', 'text_uz', 'text_ru',)
    list_display_links = list_display
