from django.urls import path
from . import views

urlpatterns = [
    path("nova/", views.vytvor_poptavku, name="vytvor_poptavku"),           # Formulář pro zadání nové poptávky
    path("odeslano/", views.poptavka_odeslana, name="poptavka_odeslana"),   # Potvrzení po odeslání
    path("", views.seznam_poptavek, name="seznam_poptavek"),                # Seznam všech poptávek
]
