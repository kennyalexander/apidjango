from django.urls import path
from .views import *


#urls de las clases a llamar segun lo necesitado
urlpatterns = [
    path('usuario/', UsuariosList.as_view(), name = 'usuario_list'),
    path('reporte/', Reporte.as_view(), name='reporte'),
    path('reportelist/', ReportList.as_view(), name='reporte_list'),
    path('solicitud/', Solicitud.as_view(), name='solicitud'),
    path('departament/', Departaments.as_view(), name='departament'),
    path('reporteupd/<int:id_reporte>/', Reportupdate.as_view(), name='report-upd'),
    path('insumoupd/<int:id_insumo>/', InsumosUpd.as_view(), name='insumo-upd')
]
