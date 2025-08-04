from django.urls import path
from . import views
from poptavky import views

urlpatterns = [
    path('', views.seznam_poptavek, name='seznam_poptavek'),
    path('nova/', views.formular_poptavky, name='formular_poptavky'),
     path('obestaveny_prostor/', views.obestaveny_prostor, name='obestaveny_prostor'),
]
