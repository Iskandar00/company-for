# Generated by Django 5.0.6 on 2024-05-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_mainview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainview',
            name='image',
            field=models.ImageField(blank=True, upload_to='main_view/image'),
        ),
    ]