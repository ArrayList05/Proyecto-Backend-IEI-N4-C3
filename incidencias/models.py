from django.db import models

# Create your models here.
class Veterinario(models.Model):
    rut = models.CharField(max_length=10,null=False)
    nombre = models.CharField(max_length=60,null=False)
    apellido = models.CharField(max_length=80,null=False)
    telefono = models.CharField(max_length=15,null=False)
    especialidad = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Duenyo(models.Model):
    rut = models.CharField(max_length=10,null=False)
    nombre = models.CharField(max_length=60,null=False)
    apellido = models.CharField(max_length=80,null=False)
    telefono = models.CharField(max_length=15,null=False)
    direccion = models.CharField(max_length=100,null=False)
    email = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Mascota(models.Model):
    nombre = models.CharField(max_length=60,null=False)
    especie = models.CharField(max_length=30,null=False)
    raza = models.CharField(max_length=50,null=False)
    edad = models.IntegerField(null=False)
    duenyo = models.ForeignKey('Duenyo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Incidencia(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Historial(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    descripcion = models.TextField(null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    descripcion = models.TextField(null=False)
    fecha_aplicacion = models.DateField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha) + " " + str(self.hora)

class Pago(models.Model):
    fecha = models.DateField(null=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    metodo_pago = models.CharField(max_length=50,null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha) + " " + str(self.monto)

class Receta(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Examen(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Diagnostico(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    motivo_diagnostico = models.CharField(max_length=100,null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class HistoriaClinica(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Consulta(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    motivo_consulta = models.CharField(max_length=100,null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Cirugia(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    motivo_cirugia = models.CharField(max_length=100,null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion    

class Hospitalizacion(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    motivo_hospitalizacion = models.CharField(max_length=100,null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion 

class Urgencia(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)
    motivo_urgencia = models.CharField(max_length=100,null=False)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion