# Generated by Django 4.2.5 on 2023-09-06 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banco',
            options={'ordering': ['nombre'], 'verbose_name': 'Banco', 'verbose_name_plural': 'Bancos'},
        ),
    ]
