from django.db import models
class CitaMedica(models.Model):
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    motivo = models.CharField(max_length=255)
    precio=models.IntegerField()
    atendido=models.BooleanField(default=False)
    def __str__(self):
        return f'Cita con {self.medico.nombre} - {self.paciente.nombre}'
 

class Medico(models.Model):
    femenino = 'femenino'
    masculino='masculino'
    genero_op = [
        ( masculino,'masculino'),
        ( femenino , 'femenino'),   
    ]
    sueldo=models.IntegerField()
    nombre = models.CharField(max_length=50)
    appat = models.CharField(max_length=50)
    apmat = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    email=models.EmailField()
    genero = models.CharField(max_length=15, choices=genero_op)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    ci = models.CharField(max_length=15)
    fecha_reg=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre+' CI: '+str(self.ci)

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()    
    def __str__(self):
        return self.nombre

class Horario(models.Model):
    MEDIO_DIA = 'Medio día'
    TARDE = 'Tarde'
    NOCHE = 'Noche'
    MANANIA='Mañana'
    COMPLETO='Tiempo Completo'
    TURNO_CHOICES = [
        (MEDIO_DIA, 'Medio día'),
        ( COMPLETO,'Tiempo Completo'),
        (TARDE, 'Tarde'),
        (NOCHE, 'Noche'),
        ( MANANIA,'Mañana')
    ]
    turno = models.CharField(max_length=50, choices=TURNO_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    descripcion = models.TextField()
    dia_semana = models.CharField(max_length=50)  # Lunes, Martes, ...
    def __str__(self):
        return self.turno+ ' '+str(self.hora_inicio)+' - '+str(self.hora_fin)
class HorarioMedico(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) 
    
class EspecialidadMedico(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    
class Paciente(models.Model):
    femenino = 'femenino'
    masculino='masculino'
    genero_op = [
        ( masculino,'masculino'),
        ( femenino , 'femenino'),   
    ]
    nombre = models.CharField(max_length=50)
    appat = models.CharField(max_length=50)
    apmat = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    genero = models.CharField(max_length=15,choices=genero_op)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    ci = models.CharField(max_length=15)
    fecha_reg=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre+' CI: '+str(self.ci)

