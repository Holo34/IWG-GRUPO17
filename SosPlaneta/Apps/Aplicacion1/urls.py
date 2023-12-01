from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"), #Cada vez que queramos crear un nuevo URL dentro de esta página, agregamos un nuevo URL (Por ejemplo un "About Us")
    path('mapa/', views.mapa, name="mapa"),
    path('historial/', views.historial, name="historial"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('test/', views.test, name='test')
]
