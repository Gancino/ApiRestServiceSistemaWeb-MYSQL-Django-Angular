from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from django.http.response import JsonResponse

from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 

from django.core.files.storage import default_storage
import os

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
        miembro.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

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

@csrf_exempt
def personaApi(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        personas_serializer = PersonaSerializer(personas, many=True)
        return JsonResponse(personas_serializer.data, safe=False)
def personaApidetail(request,pk=None):
    if request.method == 'GET': 
        try:
            persona = Persona.objects.get(id = pk)
            personas_serializer = PersonaSerializer(persona)
            return JsonResponse(personas_serializer.data, safe=False)
        except Persona.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'Person does not exist'}) 
        