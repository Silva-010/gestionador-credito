# Generated by Django 4.2.5 on 2023-11-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0012_alter_solicitudcredito_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudcredito',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
