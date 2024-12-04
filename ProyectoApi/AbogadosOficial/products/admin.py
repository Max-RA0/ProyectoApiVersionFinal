from django.contrib import admin
from .models import ServicioLegal, Divorcio, AsesoriaLegal

@admin.register(Divorcio)
class DivorcioAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo', 'num_divorcios', 'duracion_estimada')

@admin.register(AsesoriaLegal)
class AsesoriaLegalAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo', 'num_asesorias', 'especialidad')
