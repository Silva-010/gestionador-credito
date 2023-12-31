# Generated by Django 4.2.5 on 2023-09-04 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tasa_de_interes', models.DecimalField(decimal_places=2, max_digits=5)),
                ('plazo_en_meses', models.IntegerField()),
                ('fecha_creacion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
    ]
