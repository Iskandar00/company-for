from django.contrib import admin

from apps.general.models import General, Workflow, MainView


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'start_work_day', 'end_work_day', 'start_work_hour', 'end_work_hour',)
    list_display_links = list_display


@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'image', 'description_uz', 'description_ru',)
    list_display_links = list_display


@admin.register(MainView)
class MainViewAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'image',)
    list_display_links = list_display
