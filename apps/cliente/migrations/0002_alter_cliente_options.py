# Generated by Django 4.2.5 on 2023-09-04 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['fecha_registro'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]
