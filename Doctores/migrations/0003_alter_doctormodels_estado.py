# Generated by Django 4.2.16 on 2024-11-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0002_alter_doctormodels_cmp_alter_doctormodels_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodels',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
