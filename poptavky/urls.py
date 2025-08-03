from django.urls import path
from . import views

urlpatterns = [
    path("", views.seznam_poptavek, name="seznam_poptavek"),
    path("nova/", views.vytvor_poptavku, name="vytvor_poptavku"),
    path("odeslano/", views.poptavka_odeslana, name="poptavka_odeslana"),
]
