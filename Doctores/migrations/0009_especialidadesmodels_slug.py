# Generated by Django 4.2.16 on 2024-11-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0008_doctormodels_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidadesmodels',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]