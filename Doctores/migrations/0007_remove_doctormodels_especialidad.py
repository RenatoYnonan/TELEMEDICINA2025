# Generated by Django 4.2.16 on 2024-11-14 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0006_alter_doctormodels_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctormodels',
            name='especialidad',
        ),
    ]
