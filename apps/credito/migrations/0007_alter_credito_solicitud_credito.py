# Generated by Django 4.2.5 on 2023-11-28 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0009_alter_solicitudcredito_banco_and_more'),
        ('credito', '0006_alter_credito_monto_alter_credito_solicitud_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='solicitud_credito',
            field=models.OneToOneField(limit_choices_to={'estado_solicitud': 'aprobado', 'visibilidad': True}, on_delete=django.db.models.deletion.CASCADE, to='solicitud.solicitudcredito'),
        ),
    ]
