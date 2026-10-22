from rest_framework import serializers
from .models import Veterinario, Duenyo, Mascota, Incidencia, Historial, Tratamiento, Vacuna, Cita, Pago, Receta, Examen, Diagnostico, HistoriaClinica, Consulta, Cirugia, Hospitalizacion, Urgencia

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'

class DuenyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duenyo
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = '__all__'

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class CirugiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cirugia
        fields = '__all__'

class HospitalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitalizacion
        fields = '__all__'

class UrgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urgencia
        fields = '__all__'