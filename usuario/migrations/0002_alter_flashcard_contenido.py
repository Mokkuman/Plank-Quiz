# Generated by Django 4.1.dev20210924165208 on 2022-03-05 19:58

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='contenido',
            field=tinymce.models.HTMLField(max_length=1000),
        ),
    ]
