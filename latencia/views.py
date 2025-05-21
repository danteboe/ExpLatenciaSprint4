from django.http import JsonResponse
import time

# Simple dictionary cache
report_cache = {}

def generar_reporte_clinico(request, paciente_id):
    # Check if result is in cache
    if paciente_id in report_cache:
        return JsonResponse(report_cache[paciente_id])
    
    # Simulate expensive process
    time.sleep(2)  # Simulates costly process

    reporte = {
        "paciente_id": paciente_id,
        "reporte": "Resumen clínico generado automáticamente"
    }
    
    # Store in cache
    report_cache[paciente_id] = reporte
    return JsonResponse(reporte)