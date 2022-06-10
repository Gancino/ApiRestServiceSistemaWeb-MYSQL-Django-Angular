from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from django.http.response import JsonResponse

from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 

from django.core.files.storage import default_storage
import os

# Create your views here.
#Investigación
class ProyectoApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        proyectos = Proyecto.objects.all()
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return JsonResponse(proyectos_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        proyecto_serializer = ProyectoSerializer(data=request.data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': proyecto_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        proyecto = Proyecto.objects.get(id_pro=request.data['id_pro'])
        proyecto_serializer = ProyectoSerializer(proyecto, data=request.data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': proyecto_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        proyecto = Proyecto.objects.get(id_pro=id)
        proyecto.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publicproyectoApiAll(request):
    if request.method == 'GET':
        proyectos = Proyecto.objects.all()
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return JsonResponse(proyectos_serializer.data, safe=False)

def publicproyectoApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            proyecto = Proyecto.objects.get(id_pro = pk)
            proyecto_serializer = ProyectoSerializer(proyecto)
            return JsonResponse({'error': False, 'msg': 'Proyecto encontrado', 'data': proyecto_serializer.data})
        except Proyecto.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Proyecto does not exist', 'data': None})

class ArchivoApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        archivos = Archivo.objects.all()
        archivos_serializer = ArchivoSerializer(archivos, many=True)
        return JsonResponse(archivos_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        archivo_serializer = ArchivoSerializer(data=request.data)
        if archivo_serializer.is_valid():
            archivo_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': archivo_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        archivo = Archivo.objects.get(id_arch=request.data['id_arch'])
        archivo_serializer = ArchivoSerializer(archivo, data=request.data)
        if archivo_serializer.is_valid():
            archivo_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': archivo_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        archivo = Archivo.objects.get(id_arch=id)
        if(str(archivo.archivo_arch) != ''):
            if os.path.isfile(archivo.archivo_arch.path):
                os.remove(archivo.archivo_arch.path)
        archivo.delete()
        return JsonResponse("Archivo Eliminado Exitosamente!!", safe=False)

class ArchivoApiForPro(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, fk=0, *args, **kwargs):
        archivos = Archivo.objects.filter(fk_id_pro=fk)
        archivos_serializer = ArchivoSerializer(archivos, many=True)
        return JsonResponse(archivos_serializer.data, safe=False)

def publicarchivoApiAll(request):
    if request.method == 'GET':
        archivos = Archivo.objects.all()
        archivos_serializer = ArchivoSerializer(archivos, many=True)
        return JsonResponse(archivos_serializer.data, safe=False)

def publicarchivoApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            archivo = Archivo.objects.get(id_arch = pk)
            archivo_serializer = ArchivoSerializer(archivo)
            return JsonResponse({'error': False, 'msg': 'Archivo encontrado', 'data': archivo_serializer.data})
        except Archivo.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Archivo does not exist', 'data': None})

#Publicaciones
class ArticuloApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        articulos = Articulo.objects.all()
        articulos_serializer = ArticuloSerializer(articulos, many=True)
        return JsonResponse(articulos_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        articulo_serializer = ArticuloSerializer(data=request.data)
        if articulo_serializer.is_valid():
            articulo_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': articulo_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        articulo = Articulo.objects.get(id_art=request.data['id_art'])
        articulo_serializer = ArticuloSerializer(articulo, data=request.data)
        if articulo_serializer.is_valid():
            articulo_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': articulo_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        articulo = Articulo.objects.get(id_art=id)
        articulo.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publicarticuloApiAll(request):
    if request.method == 'GET':
        articulos = Articulo.objects.all()
        articulos_serializer = ArticuloSerializer(articulos, many=True)
        return JsonResponse(articulos_serializer.data, safe=False)

def publicarticuloApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            articulo = Articulo.objects.get(id_art = pk)
            articulo_serializer = ArticuloSerializer(articulo)
            return JsonResponse({'error': False, 'msg': 'Articulo encontrado', 'data': articulo_serializer.data})
        except Articulo.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Articulo does not exist', 'data': None})

class LibroApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        libros = Libro.objects.all()
        libros_serializer = LibroSerializer(libros, many=True)
        return JsonResponse(libros_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        libro_serializer = LibroSerializer(data=request.data)
        if libro_serializer.is_valid():
            libro_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': libro_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        libro = Libro.objects.get(id_lib=request.data['id_lib'])
        libro_serializer = LibroSerializer(libro, data=request.data)
        if libro_serializer.is_valid():
            libro_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': libro_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        libro = Libro.objects.get(id_lib=id)
        libro.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publiclibroApiAll(request):
    if request.method == 'GET':
        libros = Libro.objects.all()
        libros_serializer = LibroSerializer(libros, many=True)
        return JsonResponse(libros_serializer.data, safe=False)

def publiclibroApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            libro = Libro.objects.get(id_lib = pk)
            libro_serializer = LibroSerializer(libro)
            return JsonResponse({'error': False, 'msg': 'Libro encontrado', 'data': libro_serializer.data})
        except Libro.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Libro does not exist', 'data': None})

class PIntelectualApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        pintelectuales = PIntelectual.objects.all()
        pintelectuales_serializer = PIntelectualSerializer(pintelectuales, many=True)
        return JsonResponse(pintelectuales_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        pintelectual_serializer = PIntelectualSerializer(data=request.data)
        if pintelectual_serializer.is_valid():
            pintelectual_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': pintelectual_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        pintelectual = PIntelectual.objects.get(id_pin=request.data['id_pin'])
        pintelectual_serializer = PIntelectualSerializer(pintelectual, data=request.data)
        if pintelectual_serializer.is_valid():
            pintelectual_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': pintelectual_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        pintelectual = PIntelectual.objects.get(id_pin=id)
        pintelectual.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publicpintelectualApiAll(request):
    if request.method == 'GET':
        pintelectuales = PIntelectual.objects.all()
        pintelectuales_serializer = PIntelectualSerializer(pintelectuales, many=True)
        return JsonResponse(pintelectuales_serializer.data, safe=False)

def publicpintelectualApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            pintelectual = PIntelectual.objects.get(id_pin = pk)
            pintelectual_serializer = PIntelectualSerializer(pintelectual)
            return JsonResponse({'error': False, 'msg': 'Propiedad intelectual encontrada', 'data': pintelectual_serializer.data})
        except PIntelectual.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Propiedad intelectual does not exist', 'data': None})

class TesisApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        tesis = Tesis.objects.all()
        tesis_serializer = TesisSerializer(tesis, many=True)
        return JsonResponse(tesis_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        tesis_serializer = TesisSerializer(data=request.data)
        if tesis_serializer.is_valid():
            tesis_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': tesis_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        tesis = Tesis.objects.get(id_tes=request.data['id_tes'])
        tesis_serializer = TesisSerializer(tesis, data=request.data)
        if tesis_serializer.is_valid():
            tesis_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': tesis_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        tesis = Tesis.objects.get(id_tes=id)
        tesis.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publictesisApiAll(request):
    if request.method == 'GET':
        tesis = Tesis.objects.all()
        tesis_serializer = TesisSerializer(tesis, many=True)
        return JsonResponse(tesis_serializer.data, safe=False)

def publictesisApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            tesis = Tesis.objects.get(id_tes = pk)
            tesis_serializer = TesisSerializer(tesis)
            return JsonResponse({'error': False, 'msg': 'Tesis encontrada', 'data': tesis_serializer.data})
        except Tesis.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Tesis does not exist', 'data': None})

class CongresoApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        congresos = Congreso.objects.all()
        congresos_serializer = CongresoSerializer(congresos, many=True)
        return JsonResponse(congresos_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        congreso_serializer = CongresoSerializer(data=request.data)
        if congreso_serializer.is_valid():
            congreso_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': congreso_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        congreso = Congreso.objects.get(id_con=request.data['id_con'])
        congreso_serializer = CongresoSerializer(congreso, data=request.data)
        if congreso_serializer.is_valid():
            congreso_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': congreso_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        congreso = Congreso.objects.get(id_con=id)
        congreso.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publiccongresoApiAll(request):
    if request.method == 'GET':
        congresos = Congreso.objects.all()
        congresos_serializer = CongresoSerializer(congresos, many=True)
        return JsonResponse(congresos_serializer.data, safe=False)

def publiccongresoApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            congreso = Congreso.objects.get(id_con = pk)
            congreso_serializer = CongresoSerializer(congreso)
            return JsonResponse({'error': False, 'msg': 'Congreso encontrado', 'data': congreso_serializer.data})
        except Congreso.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Congreso does not exist', 'data': None})

#Miembros
class MiembroApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        miembros = Miembro.objects.all()
        miembros_serializer = MiembroSerializer(miembros, many=True)
        return JsonResponse(miembros_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        miembro_serializer = MiembroSerializer(data=request.data)
        if miembro_serializer.is_valid():
            miembro_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': miembro_serializer.data})
        return JsonResponse({'error': True, 'msg': miembro_serializer.errors, 'data': None})
        #'Error al Registrar.'
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        miembro = Miembro.objects.get(id_miem=request.data['id_miem'])
        miembro_serializer = MiembroSerializer(miembro, data=request.data)
        if miembro_serializer.is_valid():
            miembro_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': miembro_serializer.data})
        return JsonResponse({'error': True, 'msg': miembro_serializer.errors, 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        miembro = Miembro.objects.get(id_miem=id)
        if(str(miembro.imagen_miem) != ''):
            if os.path.isfile(miembro.imagen_miem.path):
                os.remove(miembro.imagen_miem.path)
        if(str(miembro.hvida_miem) != ''):
            if os.path.isfile(miembro.hvida_miem.path):
                os.remove(miembro.hvida_miem.path)
        miembro.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

class MiembroApiFilter(APIView):
    def get(self, request, tipo=0, *args, **kwargs):
        miembros = Miembro.objects.filter(tipo_miem=tipo)
        miembros_serializer = MiembroSerializer(miembros, many=True)
        return JsonResponse(miembros_serializer.data, safe=False)

def publicmiembroApiAll(request):
    if request.method == 'GET':
        miembros = Miembro.objects.all()
        miembros_serializer = MiembroSerializer(miembros, many=True)
        return JsonResponse(miembros_serializer.data, safe=False)

def  publicmiembroApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            miembro = Miembro.objects.get(id_miem = pk)
            miembro_serializer = MiembroSerializer(miembro)
            return JsonResponse({'error': False, 'msg': 'Miembro encontrado', 'data': miembro_serializer.data})
        except Miembro.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Miembro does not exist', 'data': None}) 

#Tema por usuario
class ThemeApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()
        themes_serializer = ThemeSerializer(themes, many=True)
        return JsonResponse(themes_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        theme_serializer = ThemeSerializer(data=request.data)
        if theme_serializer.is_valid():
            theme_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': theme_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        theme = Theme.objects.get(id_th=request.data['id_th'])
        theme_serializer = ThemeSerializer(theme, data=request.data)
        if theme_serializer.is_valid():
            theme_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': theme_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        theme = Theme.objects.get(id_th=id)
        theme.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

class ThemeApiDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, fk=0, *args, **kwargs):
        theme = Theme.objects.filter(fk_id_usu=fk)
        theme_serializer = ThemeSerializer(theme, many=True)
        return JsonResponse(theme_serializer.data, safe=False)

#Carousel de imágenes
class CarouselApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        carousels = Carousel.objects.all()
        carousels_serializer = CarouselSerializer(carousels, many=True)
        return JsonResponse(carousels_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        carousel_serializer = CarouselSerializer(data=request.data)
        if carousel_serializer.is_valid():
            carousel_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': carousel_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        carousel = Carousel.objects.get(id_car=request.data['id_car'])
        carousel_serializer = CarouselSerializer(carousel, data=request.data)
        if carousel_serializer.is_valid():
            carousel_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': carousel_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        carousel = Carousel.objects.get(id_car=id)
        if(str(carousel.imagen_car) != ''):
            if os.path.isfile(carousel.imagen_car.path):
                os.remove(carousel.imagen_car.path)
        carousel.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publiccarouselApiAll(request):
    if request.method == 'GET':
        carousels = Carousel.objects.all()
        carousels_serializer = CarouselSerializer(carousels, many=True)
        return JsonResponse(carousels_serializer.data, safe=False)

def  publiccarouselApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            carousel = Carousel.objects.get(id_car = pk)
            carousel_serializer = CarouselSerializer(carousel)
            return JsonResponse({'error': False, 'msg': 'Carousel de imagen encontrada', 'data': carousel_serializer.data})
        except Carousel.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Carousel de imagen does not exist', 'data': None})








# Ojo con estos views
class CategoriaApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all()
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(categorias_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        categoria_serializer = CategoriaSerializer(data=request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': categoria_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(id_cat=request.data['id_cat'])
        categoria_serializer = CategoriaSerializer(categoria, data=request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': categoria_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        categoria = Categoria.objects.get(id_cat=id)
        categoria.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publiccategoriaApiAll(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(categorias_serializer.data, safe=False)

def  publiccategoriaApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            categoria = Categoria.objects.get(id_cat = pk)
            categoria_serializer = CategoriaSerializer(categoria)
            return JsonResponse({'error': False, 'msg': 'Categoria encontrado', 'data': categoria_serializer.data})
        except Contenido.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Categoria does not exist', 'data': None})

class ContenidoApi(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        contenidos = Contenido.objects.all()
        contenidos_serializer = ContenidoSerializer(contenidos, many=True)
        return JsonResponse(contenidos_serializer.data, safe=False)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        contenido_serializer = ContenidoSerializer(data=request.data)
        if contenido_serializer.is_valid():
            contenido_serializer.save()
            return JsonResponse({'error': False,'msg': 'Registro Exitoso!!', 'data': contenido_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Registrar.', 'data': None})
    permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        contenido = Contenido.objects.get(id_con=request.data['id_con'])
        contenido_serializer = ContenidoSerializer(contenido, data=request.data)
        if contenido_serializer.is_valid():
            contenido_serializer.save()
            return JsonResponse({'error': False,'msg': 'Actualizacion Exitosa!!', 'data': contenido_serializer.data})
        return JsonResponse({'error': True, 'msg': 'Error al Actualizar', 'data': None})
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=0, *args, **kwargs):
        contenido = Contenido.objects.get(id_con=id)
        if(str(contenido.archivo_con) != ''):
            if os.path.isfile(contenido.archivo_con.path):
                os.remove(contenido.archivo_con.path)
        if(str(contenido.imagen_con) != ''):
            if os.path.isfile(contenido.imagen_con.path):
                os.remove(contenido.imagen_con.path)
        contenido.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

def publiccontenidoApiAll(request):
    if request.method == 'GET':
        contenidos = Contenido.objects.all()
        contenidos_serializer = ContenidoSerializer(contenidos, many=True)
        return JsonResponse(contenidos_serializer.data, safe=False)

def  publiccontenidoApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            contenido = Contenido.objects.get(id_con = pk)
            contenido_serializer = ContenidoSerializer(contenido)
            return JsonResponse({'error': False, 'msg': 'Contenido encontrado', 'data': contenido_serializer.data})
        except Contenido.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Contenido does not exist', 'data': None})
            
@csrf_exempt
def guardarImagen(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save('Imagenes/otros/'+file.name,file)

    return JsonResponse(file_name, safe=False)

@csrf_exempt
def guardarArchivo(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save('Archivos/'+file.name,file)

    return JsonResponse(file_name, safe=False)
        