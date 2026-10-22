from django.urls import path, include
from rest_framework import routers
from incidencias import views

router = routers.DefaultRouter()
router.register(r'veterinarios', views.VeterinarioViewSet)
router.register(r'duenyos', views.DuenyoViewSet)
router.register(r'mascotas', views.MascotaViewSet)
router.register(r'incidencias', views.IncidenciaViewSet)
router.register(r'historiales', views.HistorialViewSet)
router.register(r'tratamientos', views.TratamientoViewSet)
router.register(r'vacunas', views.VacunaViewSet)
router.register(r'citas', views.CitaViewSet)
router.register(r'pagos', views.PagoViewSet)
router.register(r'recetas', views.RecetaViewSet)
router.register(r'exámenes', views.ExamenViewSet)
router.register(r'diagnósticos', views.DiagnosticoViewSet)
router.register(r'histórias-clínicas', views.HistoriaClinicaViewSet)
router.register(r'consultas', views.ConsultaViewSet)
router.register(r'cirugías', views.CirugiaViewSet)
router.register(r'hospitalizaciones', views.HospitalizacionViewSet)
router.register(r'urgencias', views.UrgenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]