from django.contrib import admin

from apps.contacts.models import Contact, PhoneNumber, Email, Location


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message',)
    list_display_links = list_display

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'phone_number',)
    list_display_links = list_display


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'email',)
    list_display_links = list_display


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'description_uz', 'description_ru',)
    list_display_links = list_display
