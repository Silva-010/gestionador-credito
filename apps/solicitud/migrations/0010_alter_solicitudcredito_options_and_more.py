# Generated by Django 4.2.5 on 2023-11-29 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0009_alter_solicitudcredito_banco_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitudcredito',
            options={'ordering': ['-fecha_registro'], 'verbose_name': 'Solicitud de Credito', 'verbose_name_plural': 'Solicitudes de Credito'},
        ),
        migrations.AddField(
            model_name='solicitudcredito',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
