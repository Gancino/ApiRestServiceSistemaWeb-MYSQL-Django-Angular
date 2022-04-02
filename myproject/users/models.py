from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(
        _('email address'), 
        unique=True, max_length=100
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    avatar =models.ImageField(upload_to='Imagenes/User/%Y/%m', max_length=300, verbose_name='Imágen', null=True)
    work = models.CharField(verbose_name='Trabajo',max_length=100)
    direccion = models.CharField(verbose_name='Dirección',max_length=150)
    telefono = models.CharField(verbose_name='Teléfono',max_length=10)
    empresa = models.CharField(verbose_name='Empresa',max_length=150)
    descripcion = models.CharField(verbose_name='Descripción',max_length=300)