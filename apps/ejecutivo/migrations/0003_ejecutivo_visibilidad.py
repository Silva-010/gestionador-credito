# Generated by Django 4.2.5 on 2023-09-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejecutivo', '0002_alter_ejecutivo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejecutivo',
            name='visibilidad',
            field=models.BooleanField(default=True, verbose_name='Visibilidad'),
        ),
    ]
