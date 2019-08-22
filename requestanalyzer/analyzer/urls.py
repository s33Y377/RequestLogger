from django.urls import path

from .views import requestlogger

urlpatterns = [
    path('requestlogger', requestlogger),
]
