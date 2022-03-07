# Generated by Django 4.1.dev20210924165208 on 2022-03-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_flashcard_contenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='tema',
        ),
        migrations.RemoveField(
            model_name='practica',
            name='tema',
        ),
        migrations.AddField(
            model_name='flashcard',
            name='filtro',
            field=models.CharField(choices=[('Matemáticas', (('Álgebra', 'Álgebra'), ('Geometría', 'Geometría'), ('Cálculo', 'Cálculo'))), ('Español', (('Lectura y Redacción', 'Lectura y Redacción'), ('Literatura', 'Literatura'))), ('Ciencias Naturales', (('Biología', 'Biología'), ('Química', 'Química'), ('Medicina', 'Medicina'))), ('Humanidades', (('Historia', 'Historia'), ('Filosofía', 'Filosofía'), ('Psicología', 'Psicología')))], default=('Matemáticas', ('Álgebra', 'Álgebra')), max_length=50),
        ),
        migrations.AddField(
            model_name='practica',
            name='filtro',
            field=models.CharField(choices=[('Matemáticas', (('Álgebra', 'Álgebra'), ('Geometría', 'Geometría'), ('Cálculo', 'Cálculo'))), ('Español', (('Lectura y Redacción', 'Lectura y Redacción'), ('Literatura', 'Literatura'))), ('Ciencias Naturales', (('Biología', 'Biología'), ('Química', 'Química'), ('Medicina', 'Medicina'))), ('Humanidades', (('Historia', 'Historia'), ('Filosofía', 'Filosofía'), ('Psicología', 'Psicología')))], default=('Matemáticas', ('Álgebra', 'Álgebra')), max_length=50),
        ),
        migrations.DeleteModel(
            name='Tema',
        ),
    ]