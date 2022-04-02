from django.urls import re_path,path
from rest_framework.authtoken import views
from users import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'signup/', views.RegisterUsers.as_view()),
    path('update/<int:pk>/', views.UserDetails.as_view()),
    path('updateCredentials/<int:pk>/', views.UserUpdateCredentials.as_view()),
    path('info/<int:pk>/', views.UserDetails.as_view()),
    path('delete/<int:pk>/', views.UserDetails.as_view()),
    re_path(r'^guardarImagen/$', views.guardarImagen)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)