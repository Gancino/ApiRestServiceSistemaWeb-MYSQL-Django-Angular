# Generated by Django 4.0.1 on 2022-02-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_contenido_archivo_con'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='imagen_con',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Imagen'),
        ),
    ]