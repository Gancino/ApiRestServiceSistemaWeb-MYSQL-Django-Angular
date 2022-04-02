from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from users.serializers import UserSerializer

class Login(ObtainAuthToken):    
    def get(self, request, format=None):
        return Response({'detail': "GET Response"})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_serializer = UserSerializer(user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'error': False,'msg': 'Succes Login!','data': {
                'token': token.key,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_id': user.pk,
                'email': user.email,
                'password':user.password,
                'avatar': user_serializer.data.get('avatar'),
                'work': user.work,
                'direccion': user.direccion,
                'telefono': user.telefono,
                'empresa': user.empresa,
                'descripcion': user.descripcion
            }})
        return Response({'error': True, 'msg': 'No puede iniciar sesión con las credenciales proporcionadas.', 'data': None})#(status=404)

class Logout(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        request.user.auth_token.delete()
        return JsonResponse({'msg':'Sesión cerrada'})