from django.urls import path
from .views import UsuariosList, Registrar, Tabla


#urls de las clases a llamar segun lo necesitado
urlpatterns = [
    path('usuario/', UsuariosList.as_view(), name = 'usuario_list'),
    path('registrar/', Registrar.as_view(), name = 'registrar'),
    path('tabla/', Tabla.as_view(), name = 'tabla' ),
]
