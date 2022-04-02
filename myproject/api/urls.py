from django.urls import path, re_path
from api import views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('users/',views.personaApi, name='user_list'),
    path('users/<int:pk>/',views.personaApidetail, name='user_detail'),
    re_path(r'^categoria/$',views.CategoriaApi.as_view()),
    re_path(r'^categoria/([0-9]+)$',views.CategoriaApi.as_view()),
    path('public/categoriadetail/<int:pk>/',views.publiccategoriaApidetail, name='categoria_detail'),
    path('public/categoria/',views.publiccategoriaApiAll, name='categoria_all'),

    re_path(r'^contenido/$',views.ContenidoApi.as_view()),
    re_path(r'^contenido/([0-9]+)$',views.ContenidoApi.as_view()),
    path('public/contenidodetail/<int:pk>/',views.publiccontenidoApidetail, name='contenido_detail'),
    path('public/contenido/',views.publiccontenidoApiAll, name='contenido_all'),

    re_path(r'^miembro/$',views.MiembroApi.as_view()),
    re_path(r'^miembro/([0-9]+)$',views.MiembroApi.as_view()),
    path('public/miembrodetail/<int:pk>/',views.publicmiembroApidetail, name='miembro_detail'),
    path('public/miembro/',views.publicmiembroApiAll, name='miembro_all'),

    re_path(r'^theme/$',views.ThemeApi.as_view()),
    re_path(r'^theme/([0-9]+)$',views.ThemeApi.as_view()),

    re_path(r'^guardarImagen/$',views.guardarImagen),
    re_path(r'^guardarArchivo/$',views.guardarArchivo),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)