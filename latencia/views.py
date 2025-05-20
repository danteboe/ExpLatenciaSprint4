from django.views.decorators.cache import cache_page
from django.http import JsonResponse
import time

@cache_page(60 * 5)  # cache por 5 minutos
def generar_reporte_clinico(request, paciente_id):
    # Simulación de carga
    time.sleep(2)  # Simula un proceso costoso (sin caché)

    reporte = {
        "paciente_id": paciente_id,
        "reporte": "Resumen clínico generado automáticamente"
    }
    return JsonResponse(reporte)
