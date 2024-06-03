
from django.urls import path, include
from .views import index,personas

urlpatterns = [
    path('',index,name='index'),
    path('personas/',personas,name='personas')
]