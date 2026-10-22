from django.shortcuts import render
from rest_framework import viewsets
from .models import Veterinario, Duenyo, Mascota, Incidencia, Historial, Tratamiento, Vacuna, Cita, Pago, Receta, Examen, Diagnostico, HistoriaClinica, Consulta, Cirugia, Hospitalizacion, Urgencia
from .serializer import (
    VeterinarioSerializer,
    DuenyoSerializer,
    MascotaSerializer,
    IncidenciaSerializer,
    HistorialSerializer,
    TratamientoSerializer,
    VacunaSerializer,
    CitaSerializer,
    PagoSerializer,
    RecetaSerializer,
    ExamenSerializer,
    DiagnosticoSerializer,
    HistoriaClinicaSerializer,
    ConsultaSerializer,
    CirugiaSerializer,
    HospitalizacionSerializer,
    UrgenciaSerializer
)

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class DuenyoViewSet(viewsets.ModelViewSet):
    queryset = Duenyo.objects.all()
    serializer_class = DuenyoSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class CirugiaViewSet(viewsets.ModelViewSet):
    queryset = Cirugia.objects.all()
    serializer_class = CirugiaSerializer

class HospitalizacionViewSet(viewsets.ModelViewSet):
    queryset = Hospitalizacion.objects.all()
    serializer_class = HospitalizacionSerializer

class UrgenciaViewSet(viewsets.ModelViewSet):
    queryset = Urgencia.objects.all()
    serializer_class = UrgenciaSerializer


# Renderizado de página de bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html')