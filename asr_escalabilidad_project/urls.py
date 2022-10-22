from django.urls import path, include

urlpatterns = [
   path('asr/', include('asr_escalabilidad.urls'))
]