# Generated by Django 4.0.1 on 2022-01-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_categoria_miembro_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='archivo_con',
            field=models.FileField(null=True, upload_to='Archivos/%Y/%m/%d', verbose_name='Archivo'),
        ),
    ]