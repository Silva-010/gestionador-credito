# Generated by Django 4.2.5 on 2023-09-06 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_cliente_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
    ]