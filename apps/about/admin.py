from django.contrib import admin

from apps.about.models import AboutCompany, Workers, CustomerOpinion


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('text_uz', 'text_ru', 'image',)
    list_display_links = list_display


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_ru', 'image', 'position_uz', 'position_uz', 'description_uz', 'description_ru',)
    list_display_links = list_display


@admin.register(CustomerOpinion)
class CustomerOpinionAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_ru', 'position_uz', 'position_ru', 'description_uz', 'description_ru',)
    list_display_links = list_display
