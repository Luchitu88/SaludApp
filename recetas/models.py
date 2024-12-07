from django.db import models
from .validators import validar_positivos, validar_nulos, validar_maximo, validar_sexo, validar_numero, validar_letra

# Create your models here.
class Especialidad(models.Model):
    descripcion = models.CharField(max_length=50, unique=True, validators=[validar_nulos,validar_letra,])

    def __str__(self):
        return self.descripcion

class FormaFarm(models.TextChoices):
    AMP= 'amp', "Ampolla"
    COM ='com',"Comprimido"
    FCO ='fco',"Frasco"
    TUB ='tub',"Tubo"
    BOL = 'bol',"Bolsa"
    PZA = 'pza', "Pieza"

class Paciente(models.Model):
    ci=models.CharField(max_length=12,unique=True, validators=[validar_numero,])
    nombre=models.CharField(max_length=35, validators=[validar_nulos,validar_letra,])
    paterno=models.CharField(max_length=35, validators=[validar_nulos,validar_letra,])
    materno=models.CharField(max_length=35)
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=1, validators=[validar_sexo,])

    def __str__(self):
            return f'{self.ci} {self.nombre} {self.paterno} {self.materno}'

class Medico(models.Model):
    matricula=models.CharField(max_length=15, unique=True)
    nombre=models.CharField(max_length=100, validators=[validar_nulos,validar_letra])
    especialidad =models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    def __str__(self):
            return f'{self.nombre} {self.especialidad}'
    
class Medicamento(models.Model):
    liname = models.CharField(max_length=5, unique=True)
    descripcion = models.CharField(max_length=100, validators=[validar_nulos,validar_letra])
    concentracion = models.CharField(max_length=30)
    forma=models.CharField(max_length=3,
                           choices=FormaFarm.choices,
                           default=FormaFarm.COM)
    habilitado = models.BooleanField(blank=True, default=True)

    def __str__(self):
            return f'{self.liname}-{self.descripcion}-({self.concentracion})'

class Receta(models.Model):
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    diagnostico = models.TextField(validators=[validar_nulos,])
    cantidad = models.IntegerField(validators=[validar_positivos,validar_maximo,]) 
    dosis = models.TextField(validators=[validar_nulos,])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
