from django.contrib import admin

# Register your models here.

from .models import Receta, Medicamento, Medico, Paciente, Especialidad 

class EspecialidadAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)

admin.site.register(Especialidad, EspecialidadAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('ci', 'nombre', 'paterno', 'materno', 'fecha_nacimiento', 'sexo')
    ordering = ('nombre',)
    search_fields = ('ci', 'nombre', 'paterno', 'sexo' )
    list_filter = ('paterno', 'sexo',)

admin.site.register(Paciente, PacienteAdmin)

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'especialidad')
    ordering = ('nombre',)
    search_fields = ('matricula', 'nombre', 'especialidad')
    list_filter = ('especialidad',)
admin.site.register(Medico, MedicoAdmin)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('liname', 'descripcion', 'concentracion', 'forma', 'habilitado')
    ordering = ('descripcion',)
    search_fields = ('liname', 'descripcion', 'forma')
    list_filter = ('forma', 'habilitado')

admin.site.register(Medicamento, MedicamentoAdmin)

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medicamento', 'medico', 'diagnostico', 'cantidad', 'dosis')
    search_fields = ('id_paciente',)

admin.site.register(Receta, RecetaAdmin)