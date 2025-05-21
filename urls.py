from django.urls import path, include

urlpatterns = [
    path('', include('load_balancer.urls')),  # Rutas del balanceador
    path('', include('patient_manager.urls')),  # Rutas de patient_manager
    path('', include('databasse.urls')),  # Rutas de la base de  datos
]