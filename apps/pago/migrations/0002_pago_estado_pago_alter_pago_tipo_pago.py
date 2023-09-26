# Generated by Django 4.2.5 on 2023-09-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='estado_pago',
            field=models.CharField(choices=[('realizado', 'Realizado'), ('atrasado', 'Atrasado'), ('otros', 'Otros')], default='realizado', max_length=20),
        ),
        migrations.AlterField(
            model_name='pago',
            name='tipo_pago',
            field=models.CharField(choices=[('principal', 'Principal'), ('interes', 'Interés'), ('otros', 'Otros')], default='principal', max_length=20),
        ),
    ]