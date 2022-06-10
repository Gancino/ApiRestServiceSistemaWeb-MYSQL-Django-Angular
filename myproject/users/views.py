from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from users.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .serializers import *
from rest_framework.parsers import FileUploadParser
import os

class RegisterUsers(APIView):
    #Create
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        register = UserSerializer(data=request.data)

        if register.is_valid():
            user = register.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return JsonResponse({'msg': 'Usuario registrado correctamente!!'})
        else:
            #if (register.errors.get('email')):
            #    print('error en el email')
            return JsonResponse({'msg': register.errors}) 

class UserDetails(APIView):
    #Index
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk=0, *args, **kwargs):
        try:
            user = User.objects.get(id=pk)
            user_serializer = UserSerializer(user)
            return JsonResponse({'error': False, 'msg': 'Usuario encontrado', 'data': user_serializer.data})
        except User.DoesNotExist:
            return JsonResponse({'error': True, 'msg': 'User does not exist', 'data': None})

    #Update
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk=0, *args, **kwargs):
        user = User.objects.get(id=pk)
        updateUser = UserSerializerPerfil(user, data=request.data)
        if updateUser.is_valid():
            user = updateUser.save()
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'error': False,'msg': 'Cuenta actualizada correctamente!!','data': {
                'token': token.key,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_id': user.pk,
                'email': user.email,
                'password':user.password,
                'avatar': updateUser.data.get('avatar'),
                'work': user.work,
                'direccion': user.direccion,
                'telefono': user.telefono,
                'empresa': user.empresa,
                'descripcion': user.descripcion
            } })
        else:
            return JsonResponse({'error': True, 'msg': updateUser.errors, 'data': None})
    
    #delete
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        if(str(user.avatar) != ''):
            if os.path.isfile(user.avatar.path):
                os.remove(user.avatar.path)
        user.delete()
        return JsonResponse({'msg': 'Usuario eliminado!!'})

class UserUpdateCredentials(APIView):
    #Update
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk=0, *args, **kwargs):
        user = User.objects.get(id=pk)
        updateUser = UserSerializerCredentials(user, data=request.data)
        if updateUser.is_valid():
            user = updateUser.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'error': False,'msg': 'Credenciales actualizados correctamente!!','data': {
                'token': token.key,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_id': user.pk,
                'email': user.email,
                'password':user.password,
                'avatar': updateUser.data.get('avatar'),
                'work': user.work,
                'direccion': user.direccion,
                'telefono': user.telefono,
                'empresa': user.empresa,
                'descripcion': user.descripcion
            } })
        else:
            return JsonResponse({'error': True, 'msg': updateUser.errors, 'data': None})




@csrf_exempt
def guardarImagen(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save('Imagenes/User/'+file.name,file)

    return JsonResponse(file_name, safe=False)