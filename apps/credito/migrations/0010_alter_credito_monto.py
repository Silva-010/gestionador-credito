# Generated by Django 4.2.5 on 2023-12-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0009_alter_credito_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='monto',
            field=models.CharField(),
        ),
    ]
