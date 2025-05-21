from django.urls import path
from .views import load_balance_report

urlpatterns = [
    path('report/<int:paciente_id>', load_balance_report, name='load_balance_report'),
]