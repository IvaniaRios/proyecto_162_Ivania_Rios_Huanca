from django.contrib import admin
from .models import Paciente,Medico,Especialidad,Horario,HorarioMedico,EspecialidadMedico,CitaMedica
class PacienteAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_reg",)
class MedicoAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_reg",)
class EspecialidadAdmin(admin.ModelAdmin):
    readonly_fields=("id",)
class HorariodAdmin(admin.ModelAdmin):
    readonly_fields=("id",)
class MedicoHorariodAdmin(admin.ModelAdmin):
    readonly_fields=("id",)
class EspecialidadMedicoAdmin(admin.ModelAdmin):
    readonly_fields=("id",)
class HorarioMedicoAdmin(admin.ModelAdmin):
    readonly_fields=("id",)
class CitaMedicaAdmin(admin.ModelAdmin):
    readonly_fields=("id",)

admin.site.register(CitaMedica,CitaMedicaAdmin)
admin.site.register(HorarioMedico,HorarioMedicoAdmin)
admin.site.register(EspecialidadMedico,EspecialidadMedicoAdmin)
admin.site.register(Horario,HorariodAdmin)
admin.site.register(Especialidad,EspecialidadAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Paciente,PacienteAdmin)
