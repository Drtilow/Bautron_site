from django.urls import path
from . import views
from poptavky import views

urlpatterns = [
    path('', views.seznam_poptavek, name='seznam_poptavek'),
    path('nova/', views.formular_poptavky, name='formular_poptavky'),
    path('obestaveny_prostor/', views.obestaveny_prostor, name='obestaveny_prostor'),
    path("o-nas/", views.o_nas, name="o_nas"),
    path("zasady-ochrany/", views.zasady_ochrany, name="zasady_ochrany"),


]
