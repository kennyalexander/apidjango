from django.urls import path
from .views import UsuariosList

urlpatterns = [
    path('usuario/', UsuariosList.as_view(), name = 'usuario_list'),
    # path('registrar/', Registrar.as_view(), name = 'registrar_user')
]
