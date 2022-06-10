from django.urls import path, re_path
from api import views

from django.conf.urls.static import static
from django.conf import settings

# Create your urls here.
urlpatterns = [
  #Investigación
  re_path(r'^proyecto/$',views.ProyectoApi.as_view()),
  re_path(r'^proyecto/([0-9]+)$',views.ProyectoApi.as_view()),
  path('public/proyectodetail/<int:pk>/',views.publicproyectoApidetail, name='proyecto_detail'),
  path('public/proyecto/',views.publicproyectoApiAll, name='proyecto_all'),

  #Archivos por proyecto
  re_path(r'^archivo/$',views.ArchivoApi.as_view()),
  re_path(r'^archivo/([0-9]+)$',views.ArchivoApi.as_view()),
  re_path(r'^archivoproyecto/([0-9]+)$',views.ArchivoApiForPro.as_view()),
  path('public/archivodetail/<int:pk>/',views.publicarchivoApidetail, name='archivo_detail'),
  path('public/archivo/',views.publicarchivoApiAll, name='archivo_all'),

  #Publicaciones
  re_path(r'^articulo/$',views.ArticuloApi.as_view()),
  re_path(r'^articulo/([0-9]+)$',views.ArticuloApi.as_view()),
  path('public/articulodetail/<int:pk>/',views.publicarticuloApidetail, name='articulo_detail'),
  path('public/articulo/',views.publicarticuloApiAll, name='articulo_all'),

  re_path(r'^libro/$',views.LibroApi.as_view()),
  re_path(r'^libro/([0-9]+)$',views.LibroApi.as_view()),
  path('public/librodetail/<int:pk>/',views.publiclibroApidetail, name='libro_detail'),
  path('public/libro/',views.publiclibroApiAll, name='libro_all'),

  re_path(r'^pintelectual/$',views.PIntelectualApi.as_view()),
  re_path(r'^pintelectual/([0-9]+)$',views.PIntelectualApi.as_view()),
  path('public/pintelectualdetail/<int:pk>/',views.publicpintelectualApidetail, name='pintelectual_detail'),
  path('public/pintelectual/',views.publicpintelectualApiAll, name='pintelectual_all'),

  re_path(r'^tesis/$',views.TesisApi.as_view()),
  re_path(r'^tesis/([0-9]+)$',views.TesisApi.as_view()),
  path('public/tesisdetail/<int:pk>/',views.publictesisApidetail, name='tesis_detail'),
  path('public/tesis/',views.publictesisApiAll, name='tesis_all'),

  re_path(r'^congreso/$',views.CongresoApi.as_view()),
  re_path(r'^congreso/([0-9]+)$',views.CongresoApi.as_view()),
  path('public/congresodetail/<int:pk>/',views.publiccongresoApidetail, name='congreso_detail'),
  path('public/congreso/',views.publiccongresoApiAll, name='congreso_all'),

  #Miembros
  re_path(r'^miembro/$',views.MiembroApi.as_view()),
  re_path(r'^miembro/([0-9]+)$',views.MiembroApi.as_view()),
  re_path(r'^public/miembrofilter/([0-9]+)$',views.MiembroApiFilter.as_view()),
  path('public/miembro/',views.publicmiembroApiAll, name='miembro_all'),
  path('public/miembrodetail/<int:pk>/',views.publicmiembroApidetail, name='miembro_detail'),

  #Tema por usuario
  re_path(r'^theme/$',views.ThemeApi.as_view()),
  re_path(r'^theme/([0-9]+)$',views.ThemeApi.as_view()),
  re_path(r'^themedetail/([0-9]+)$',views.ThemeApiDetail.as_view()),

  #Carousel de imágenes
  re_path(r'^carousel/$',views.CarouselApi.as_view()),
  re_path(r'^carousel/([0-9]+)$',views.CarouselApi.as_view()),
  path('public/carouseldetail/<int:pk>/',views.publiccarouselApidetail, name='carousel_detail'),
  path('public/carousel/',views.publiccarouselApiAll, name='carousel_all'),




  # Ojo con estas urls
  re_path(r'^categoria/$',views.CategoriaApi.as_view()),
  re_path(r'^categoria/([0-9]+)$',views.CategoriaApi.as_view()),
  path('public/categoriadetail/<int:pk>/',views.publiccategoriaApidetail, name='categoria_detail'),
  path('public/categoria/',views.publiccategoriaApiAll, name='categoria_all'),

  re_path(r'^contenido/$',views.ContenidoApi.as_view()),
  re_path(r'^contenido/([0-9]+)$',views.ContenidoApi.as_view()),
  path('public/contenidodetail/<int:pk>/',views.publiccontenidoApidetail, name='contenido_detail'),
  path('public/contenido/',views.publiccontenidoApiAll, name='contenido_all'),

  re_path(r'^guardarImagen/$',views.guardarImagen),
  re_path(r'^guardarArchivo/$',views.guardarArchivo),



  #obsoleto
  #path('users/',views.personaApi, name='user_list'),
  #path('users/<int:pk>/',views.personaApidetail, name='user_detail')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)