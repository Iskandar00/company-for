from django.db import models

from apps.general.services import field_language


class ServiceType(models.Model):
    title_uz = models.CharField(max_length=75)
    title_ru = models.CharField(max_length=75, blank=True)
    image = models.ImageField(upload_to='service_type/image', blank=True, null=True)
    text_uz = models.TextField(max_length=2000)
    text_ru = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.title_uz

    @property
    def title(self):
        return field_language(self, 'title')

    @property
    def text(self):
        return field_language(self, 'text')
