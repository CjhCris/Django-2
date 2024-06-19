from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('alumnos/index', views.index, name='alumnos/index'),
    path('crud', views.crud, name='crud'),
]


