# Generated by Django 4.2.16 on 2024-11-13 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0003_alter_doctormodels_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctormodels',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'Doctores'},
        ),
    ]