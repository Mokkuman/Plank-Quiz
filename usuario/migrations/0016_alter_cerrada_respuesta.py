# Generated by Django 4.0 on 2022-04-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_alter_cerrada_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerrada',
            name='respuesta',
            field=models.CharField(max_length=100),
        ),
    ]