# Generated by Django 4.0.1 on 2022-02-10 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_miembro_imagen_miem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='imagen_miem',
            field=models.ImageField(max_length=300, null=True, upload_to='Imagenes/Miembros/', verbose_name='Foto'),
        ),
    ]