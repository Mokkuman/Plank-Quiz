# Generated by Django 4.0.1 on 2022-05-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0019_alter_flashcard_thumbnail_alter_practica_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='thumbnail',
            field=models.ImageField(blank=True, default='planky.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='practica',
            name='thumbnail',
            field=models.ImageField(blank=True, default='planky.png', null=True, upload_to=''),
        ),
    ]
