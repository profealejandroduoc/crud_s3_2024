
from django.urls import path, include
from .views import index,personas,detallepersona, crearpersona,modificarpersona,eliminarpersona

#PARA TRABAJAR CON IMAGENES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('personas/',personas,name='personas'),
    path('detallepersona/<id>',detallepersona,name='detallepersona'),
    path('crearpersona/',crearpersona,name='crearpersona'),
    path('modificarpersona/<id>',modificarpersona, name='modificarpersona'),
    path('eliminarpersona/<id>', eliminarpersona, name='eliminarpersona'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)