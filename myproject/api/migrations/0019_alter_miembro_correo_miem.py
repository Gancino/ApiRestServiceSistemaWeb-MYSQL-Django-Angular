# Generated by Django 4.0.1 on 2022-02-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_miembro_correo_miem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='correo_miem',
            field=models.CharField(max_length=100, unique=True, verbose_name='Correo'),
        ),
    ]
