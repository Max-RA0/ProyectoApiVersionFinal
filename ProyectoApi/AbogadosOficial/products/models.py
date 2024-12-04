from django.db import models

# Modelo base para servicios legales
class ServicioLegal(models.Model):
    nombre_servicio = models.CharField(
        max_length=255, 
        unique=True, 
        db_column='nombre_servicio'
    )
    descripcion = models.CharField(
        max_length=255, 
        db_column='descripcion'
    )
    costo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        db_column='costo'
    )

    def mostrar_info(self):
        return f"Nombre: {self.nombre_servicio}, Descripción: {self.descripcion}, Costo: {self.costo}"

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        abstract = False
        verbose_name = "Servicio Legal"
        verbose_name_plural = "Servicios Legales"


# Modelo específico para servicios de divorcio
class Divorcio(ServicioLegal):
    num_divorcios = models.IntegerField(
        db_column='num_divorcios'
    )  # Número de divorcios manejados
    duracion_estimada = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        db_column='duracion_estimada'
    )  # Duración estimada en años

    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre_servicio}, Descripción: {self.descripcion}, "
            f"Costo: {self.costo}, Número de Divorcios: {self.num_divorcios}, "
            f"Duración Estimada: {self.duracion_estimada} años"
        )
    
    @staticmethod
    def calcular_impuesto(costo, num_divorcios):
        return costo * num_divorcios
    
    class Meta:
        verbose_name = "Servicio de Divorcio"
        verbose_name_plural = "Servicios de Divorcio"


# Modelo específico para asesorías legales
class AsesoriaLegal(ServicioLegal):
    num_asesorias = models.IntegerField(
        db_column='num_asesorias'
    )  # Número de asesorías realizadas
    especialidad = models.CharField(
        max_length=255, 
        db_column='especialidad'
    )  # Especialidad del servicio

    def mostrar_info(self):
        return (
            f"Nombre: {self.nombre_servicio}, Descripción: {self.descripcion}, "
            f"Costo: {self.costo}, Especialidad: {self.especialidad}"
        )
        
    @staticmethod
    def calcular_impuestos(costo, num_asesorias):
        return costo * num_asesorias

    class Meta:
        verbose_name = "Asesoría Legal"
        verbose_name_plural = "Asesorías Legales"
