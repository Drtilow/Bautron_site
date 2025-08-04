from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_poptavek, name='seznam_poptavek'),
    path('nova/', views.formular_poptavky, name='formular_poptavky'),
]
