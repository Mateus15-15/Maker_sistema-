from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.cliente, name='cliente'),
]
