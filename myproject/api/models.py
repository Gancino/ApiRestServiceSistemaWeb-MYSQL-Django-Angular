from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True,verbose_name='Codigo')
    nombre_cat = models.CharField(max_length=100,verbose_name='Categoria')

    def __str__(self):
        return self.nombre_cat
    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'
        db_table= 'categoria'
        ordering=['id_cat']

class Contenido(models.Model):
    id_con = models.AutoField(primary_key=True,verbose_name='Codigo')
    titulo_con = models.CharField(max_length=100,verbose_name='Título')
    descripcion_con = models.CharField(max_length=500,verbose_name='Descripción')
    archivo_con = models.FileField(upload_to='Archivos/Contenido/%Y/%m', max_length=300, verbose_name='Archivo', null=True)
    imagen_con=models.ImageField(upload_to='Imagenes/Contenido/%Y/%m', max_length=300, verbose_name='Imagen', null=True)
    fecha_con = models.DateField(verbose_name="Fecha", null=True)
    autor_con = models.CharField(max_length=100, verbose_name='Autor')
    fk_id_cat= models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.titulo_con
    class Meta:
        verbose_name= 'Contenido'
        verbose_name_plural= 'Contenidos'
        db_table= 'contenido'
        ordering=['id_con']

class Miembro(models.Model):
    id_miem = models.AutoField(primary_key=True,verbose_name='Codigo')
    nombre_miem = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_miem = models.CharField(max_length=100, verbose_name='Apellidos')
    correo_miem = models.CharField(max_length=100, verbose_name='Correo', unique=True)
    telefono_miem = models.CharField(max_length=10, verbose_name='Telefono')
    imagen_miem = models.ImageField(upload_to='Imagenes/Miembros/%Y/%m', max_length=300, verbose_name='Foto', null=True)
    cargo_miem = models.CharField(max_length=100, verbose_name='Cargo', null=True)
    descripcion_miem = models.CharField(max_length=500, verbose_name='Descripción', null=True)

    def __str__(self):
        return self.nombre_miem + " " + self.apellido_miem
    class Meta:
        verbose_name= 'Miembro'
        verbose_name_plural= 'Miembros'
        db_table= 'miembro'
        ordering=['id_miem']

class Theme(models.Model):
    id_th = models.AutoField(primary_key=True,verbose_name='Codigo')
    nombre_th = models.CharField(max_length=100,verbose_name='Tema')
    posicion_th = models.CharField(max_length=10,verbose_name='Posicion')
    def __str__(self):
        return self.nombre_th
    class Meta:
        verbose_name= 'Tema'
        verbose_name_plural= 'Temas'
        db_table= 'theme'
        ordering=['id_th']




class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.CharField('Avatar', max_length=300)
    name = models.CharField('Nombre',max_length=100)
    gender = models.CharField('Genero',max_length=10, null=True, blank=True)
    age = models.IntegerField('Edad')
    description = models.CharField('Descripcion', max_length=200)
    work = models.CharField('Trabajo', null=True, max_length=100, blank=True)

    def __str__(self):
        return '{0},{1}'.format(self.id,self.name,self.age)