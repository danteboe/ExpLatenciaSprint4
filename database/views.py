from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import redis
import json

# Conectar a Redis en la misma VM
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@require_http_methods(["GET", "POST"])
def report_cache(request, paciente_id):
    if request.method == "GET":
        # Verificar si el reporte está en caché
        cached_report = redis_client.get(f"report:{paciente_id}")
        if cached_report:
            # Retornar el reporte cacheado
            return JsonResponse(json.loads(cached_report))
        # Retornar error si no está en caché
        return JsonResponse({"error": "Reporte no encontrado"}, status=404)

    elif request.method == "POST":
        # Obtener el reporte del cuerpo de la solicitud
        try:
            reporte = json.loads(request.body)
            # Validar que el reporte tenga paciente_id y coincida
            if reporte.get("paciente_id") != paciente_id:
                return JsonResponse({"error": "ID de paciente no coincide"}, status=400)
            # Almacenar en Redis con expiración de 5 minutos
            redis_client.setex(f"report:{paciente_id}", 60 * 5, json.dumps(reporte))
            # Retornar el reporte almacenado
            return JsonResponse(reporte)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Cuerpo de la solicitud inválido"}, status=400)