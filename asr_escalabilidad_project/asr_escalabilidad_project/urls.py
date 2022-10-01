from django.urls import path, include
from . import views
urlpatterns = [
   path('asr/', include('asr_escalabilidad.urls')),
   path('health-check/', views.healthCheck)
]