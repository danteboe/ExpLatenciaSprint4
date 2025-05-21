from django.urls import path
from .views import generar_reporte_clinico

urlpatterns = [
    path('patient/report/<int:paciente_id>', generar_reporte_clinico, name='generar_reporte_clinico'),
]