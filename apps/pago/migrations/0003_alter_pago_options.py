# Generated by Django 4.2.5 on 2023-09-06 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0002_pago_estado_pago_alter_pago_tipo_pago'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pago',
            options={'ordering': ['fecha_pago'], 'verbose_name': 'Pago', 'verbose_name_plural': 'Pagos'},
        ),
    ]