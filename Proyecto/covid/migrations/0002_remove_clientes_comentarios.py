# Generated by Django 3.0.3 on 2020-07-09 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='comentarios',
        ),
    ]