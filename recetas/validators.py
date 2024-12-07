from django.core.exceptions import ValidationError

def validar_positivos(value):
    if value < 1:
        raise ValidationError('La cantidad de medicamento %(value)s debe ser mayor a 0', params={'value':value})
    
def validar_maximo(value):
    if value > 100:
        raise ValidationError('La cantidad de medicamento de %(value)s no debe ser mayor a 100', params={'value':value})
    
def validar_nulos(value):
    #if len(value) <= 1:
    if not value:
        raise ValidationError('El campo no puede estar vacio', params={'value':value})
    
def validar_sexo(value):
    if value not in ['M', 'F']:
        raise ValidationError('El genero %(value)s debe ser M (masculino) o F (femenino)', params={'value':value})
    
#****
def validar_numero(value):
    if not value.isdigit():
        raise ValidationError('El valor %(value)s debe contener solos numeros', params={'value':value})
    
def validar_letra(value):
    if not value.isalpha():
        raise ValidationError('El valor %(value)s debe contener solo letras', params={'value':value})