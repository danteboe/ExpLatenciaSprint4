from django.http import JsonResponse
import requests
import itertools

# Lista de instancias de patient_manager
INSTANCES = [
    "http://<vm-reporte-clinico-1>:8000",
    "http://<vm-reporte-clinico-2>:8000",
]

# Iterador para round-robin
instance_cycle = itertools.cycle(INSTANCES)

def load_balance_report(request, paciente_id):
    # Seleccionar la siguiente instancia en modo round-robin
    target_instance = next(instance_cycle)
    
    # Construir la URL de la instancia para el reporte
    target_url = f"{target_instance}/patient/report/{paciente_id}"
    
    try:
        # Redirigir la solicitud GET a la instancia seleccionada
        response = requests.get(target_url, timeout=5)
        
        # Verificar si la respuesta es válida
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            # Manejar errores de la instancia
            return JsonResponse({"error": f"Error en la instancia {target_instance}: {response.status_code}"}, status=response.status_code)
    
    except requests.RequestException as e:
        # Manejar errores de conexión o timeout
        return JsonResponse({"error": f"Fallo al conectar con {target_instance}: {str(e)}"}, status=503)