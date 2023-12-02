# Generated by Django 4.2.5 on 2023-11-27 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0004_banco_direccion_banco_telefono'),
        ('cliente', '0007_alter_cliente_options'),
        ('solicitud', '0008_alter_solicitudcredito_estado_solicitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudcredito',
            name='banco',
            field=models.ForeignKey(limit_choices_to={'visibilidad': True}, on_delete=django.db.models.deletion.CASCADE, to='banco.banco'),
        ),
        migrations.AlterField(
            model_name='solicitudcredito',
            name='cliente',
            field=models.ForeignKey(limit_choices_to={'visibilidad': True}, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
    ]