# Generated by Django 4.2.5 on 2023-12-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0015_alter_solicitudcredito_fecha_aprobacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudcredito',
            name='fecha_aprobacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
