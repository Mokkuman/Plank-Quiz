# Generated by Django 4.1.dev20210924165208 on 2022-04-15 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_user_imagenperfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votopract',
            name='id_practica',
        ),
        migrations.RemoveField(
            model_name='votopract',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='VotoFlash',
        ),
        migrations.DeleteModel(
            name='VotoPract',
        ),
    ]
