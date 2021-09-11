from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('config/', views.stripe_config),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('cancel/', views.cancelMsg, name="cancel"),
    path('donations/', views.donations, name="donations"),
]
