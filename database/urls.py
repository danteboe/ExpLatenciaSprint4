from django.urls import path
from .views import report_cache

urlpatterns = [
    path('api/report/<int:paciente_id>', report_cache, name='report_cache'),
]