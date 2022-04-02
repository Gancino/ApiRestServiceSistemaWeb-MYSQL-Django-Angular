# Generated by Django 4.0.1 on 2022-01-26 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_cat', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre_cat', models.CharField(max_length=100, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
                'ordering': ['id_cat'],
            },
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id_miem', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre_miem', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellido_miem', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('correo_miem', models.CharField(max_length=200, verbose_name='Correo')),
                ('telefono_miem', models.CharField(max_length=10, verbose_name='Telefono')),
                ('imagen_miem', models.CharField(max_length=100, null=True, verbose_name='Foto')),
                ('cargo_miem', models.CharField(max_length=100, null=True, verbose_name='Cargo')),
                ('descripcio_miem', models.CharField(max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Miembro',
                'verbose_name_plural': 'Miembros',
                'db_table': 'miembro',
                'ordering': ['id_miem'],
            },
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id_con', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('titulo_con', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion_con', models.CharField(max_length=500, verbose_name='Descripción')),
                ('archivo_con', models.FileField(upload_to='Archivos/%Y/%m/%d', verbose_name='Archivo')),
                ('imagen_con', models.CharField(max_length=100, null=True, verbose_name='Imagen')),
                ('fecha_con', models.DateField(verbose_name='Fecha')),
                ('autor_con', models.CharField(max_length=100, verbose_name='Autor')),
                ('fk_id_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Contenido',
                'verbose_name_plural': 'Contenidos',
                'db_table': 'contenido',
                'ordering': ['id_con'],
            },
        ),
    ]
