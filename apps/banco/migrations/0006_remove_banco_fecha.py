# Generated by Django 4.2.5 on 2023-12-04 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0005_banco_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banco',
            name='fecha',
        ),
    ]