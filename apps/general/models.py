from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _, get_language

from apps.general.services import field_language
from apps.general.validate import phone_number_validate


class General(models.Model):

    class DaysOfTheWeek(models.TextChoices):
        Mo = 'mon', _('monday')
        Tu = 'tue', _('tuesday')
        We = 'wed', _('wednesday')
        Th = 'thu', _('thursday')
        Fr = 'fri', _('friday')
        Sa = 'sat', _('saturday')
        Su = 'sun', _('sunday')

    phone_number = models.CharField(max_length=13, validators=[phone_number_validate])
    email = models.EmailField()
    start_work_day = models.CharField(max_length=3, choices=DaysOfTheWeek.choices)
    end_work_day = models.CharField(max_length=3, choices=DaysOfTheWeek.choices)
    start_work_hour = models.TimeField()
    end_work_hour = models.TimeField()
    logo = models.ImageField(upload_to='general/logo')
    description_name_uz = models.CharField(max_length=75)
    description_name_ru = models.CharField(max_length=75)
    description_uz = models.TextField(max_length=1000)
    description_ru = models.TextField(max_length=1000)

    @property
    def description_name(self):
        return field_language(self, 'description_name')

    @property
    def description(self):
        return field_language(self, 'description')

    def clean(self):
        if not (self.start_work_hour < self.end_work_hour):
            raise ValidationError(_('end_work_hour must be greater than start_work_hour.'))


class Workflow(models.Model):
    title_uz = models.CharField(max_length=75)
    title_ru = models.CharField(max_length=75)
    image = models.ImageField(upload_to='workers/image')
    description_uz = models.CharField(max_length=1000)
    description_ru = models.CharField(max_length=1000)

    def __str__(self):
        return self.title_uz

    @property
    def title(self):
        return field_language(self, 'title')

    @property
    def description(self):
        return field_language(self, 'description')


class MainView(models.Model):
    title_uz = models.CharField(max_length=150)
    title_ru = models.CharField(max_length=150)
    short_description_uz = models.CharField(max_length=75)
    short_description_ru = models.CharField(max_length=75)
    long_description_uz = models.CharField(max_length=700)
    long_description_ru = models.CharField(max_length=700)
    image = models.ImageField(upload_to='main_view/image', blank=True, null=True)

    @property
    def title(self):
        return field_language(self, 'title')

    @property
    def short_description(self):
        return field_language(self, 'short_description')

    @property
    def long_description(self):
        return field_language(self, 'long_description')
