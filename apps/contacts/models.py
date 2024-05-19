from django.db import models

from apps.general.validate import normalize_text, phone_number_validate
from apps.general.services import field_language


class Contact(models.Model):
    full_name = models.CharField(max_length=75)
    email = models.EmailField()
    subject = models.CharField(max_length=75, blank=True)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return f'{self.full_name}: {self.subject}'

    def fields(self):
        return [
            'full_name',
            'email',
            'subject',
            'message',
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class PhoneNumber(models.Model):
    title_uz = models.CharField(max_length=30)
    title_ru = models.CharField(max_length=30)
    description_uz = models.CharField(max_length=300)
    description_ru = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13, validators=[phone_number_validate])

    @property
    def title(self):
        return field_language(self, 'title')

    @property
    def description(self):
        return field_language(self, 'description')


class Email(models.Model):
    title_uz = models.CharField(max_length=30)
    title_ru = models.CharField(max_length=30)
    description_uz = models.CharField(max_length=300)
    description_ru = models.CharField(max_length=300)
    email = models.EmailField()

    @property
    def title(self):
        return field_language(self, 'title')

    @property
    def description(self):
        return field_language(self, 'description')


class Location(models.Model):
    title_uz = models.CharField(max_length=30)
    title_ru = models.CharField(max_length=30)
    description_uz = models.CharField(max_length=300)
    description_ru = models.CharField(max_length=300)

