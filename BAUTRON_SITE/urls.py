from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Vítejte na hlavní stránce systému BAUTRON!")

def hello(request):
    return HttpResponse("Testovací stránka Django běží!")

urlpatterns = [
    path('', home),  # nyní domovská stránka dostupná na /
    path('test/', hello),
    path('admin/', admin.site.urls),
]
