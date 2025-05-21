from django.http import JsonResponse
import time
import requests
import json

# URL base de la API de cache en vm-db-redis
DB_API_URL = "http://<vm-db-ip>:8000/api/report/"

def generar_reporte_clinico(request, paciente_id):
    # Verificar si el reporte está en caché enviando solicitud GET
    response = requests.get(f"{DB_API_URL}{paciente_id}")
    if response.status_code == 200:
        # Retornar inmediatamente el reporte cacheado
        return JsonResponse(response.json())
    
    # Simular un proceso costoso
    time.sleep(2)

    # Generar el reporte
    reporte = {
        "paciente_id": paciente_id,
        "reporte": "Resumen clínico generado automáticamente"
    }
    
    # Almacenar en la base de datos enviando solicitud POST
    requests.post(f"{DB_API_URL}{paciente_id}", json=reporte)
    
    # Retornar el reporte generado
    return JsonResponse(reporte)