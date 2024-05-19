from django.db import models

from apps.general.services import field_language


class AboutCompany(models.Model):
    text_uz = models.TextField(max_length=2000)
    text_ru = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='about_company/image')

    def __str__(self):
        return self.text_uz

    @property
    def text(self):
        return field_language(self, 'text')


class Workers(models.Model):
    name_uz = models.CharField(max_length=75)
    name_ru = models.CharField(max_length=75)
    image = models.ImageField(upload_to='workers/image')
    position_uz = models.CharField(max_length=150)
    position_ru = models.CharField(max_length=150)
    description_uz = models.CharField(max_length=300)
    description_ru = models.CharField(max_length=300)

    def __str__(self):
        return self.name_uz

    @property
    def name(self):
        return field_language(self, 'name')

    @property
    def position(self):
        return field_language(self, 'position')

    @property
    def description(self):
        return field_language(self, 'description')


class CustomerOpinion(models.Model):
    name_uz = models.CharField(max_length=75)
    name_ru = models.CharField(max_length=75, blank=True)
    position_uz = models.CharField(max_length=150)
    position_ru = models.CharField(max_length=150)
    description_uz = models.CharField(max_length=300)
    description_ru = models.CharField(max_length=300)

    def __str__(self):
        return self.name_uz

    @property
    def name(self):
        return field_language(self, 'name')

    @property
    def position(self):
        return field_language(self, 'position')

    @property
    def description(self):
        return field_language(self, 'description')


