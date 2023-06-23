from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


#urls de las clases a llamar segun lo necesitado
urlpatterns = [
    path('usuario/', UsuariosList.as_view(), name = 'usuario_list'),
    path('reporte/', Reportepost.as_view(), name='reporte'),
    path('reportelist/', ReportList.as_view(), name='reporte_list'),
    path('solicitudpost/', SolicitudPost.as_view(), name='solicitud'),
    path('reporteupd/<int:id_reporte>/', Reportupdate.as_view(), name='report-upd'),
    path('insumoupd/<int:id_insumo>/', InsumosUpd.as_view(), name='insumo-upd'),
    path('insumolist/', InsumoList.as_view(), name='insumos_list'),
    path('solicitudlist/', SolicitudList.as_view(), name='solicitud_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 