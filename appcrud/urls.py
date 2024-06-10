
from django.urls import path, include
from .views import index,personas

#PARA TRABAJAR CON IMAGENES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('personas/',personas,name='personas')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)