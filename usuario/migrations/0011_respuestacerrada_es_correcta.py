# Generated by Django 4.0 on 2022-03-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_remove_votoflash_neutro_remove_votopract_neutro'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestacerrada',
            name='es_correcta',
            field=models.BooleanField(default=False),
        ),
    ]
