# Generated by Django 4.2.5 on 2023-09-06 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0003_alter_credito_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credito',
            options={'ordering': ['fecha_creacion'], 'verbose_name': 'Credito', 'verbose_name_plural': 'Creditos'},
        ),
    ]