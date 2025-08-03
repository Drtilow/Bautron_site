from django.shortcuts import render, redirect
from .models import Poptavka
from .forms import PoptavkaForm

# Seznam všech poptávek
def seznam_poptavek(request):
    poptavky = Poptavka.objects.all()
    return render(request, "poptavky/seznam.html", {"poptavky": poptavky})

# Formulář pro vytvoření nové poptávky
def vytvor_poptavku(request):
    if request.method == "POST":
        form = PoptavkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("poptavka_odeslana")
    else:
        form = PoptavkaForm()
    return render(request, "poptavky/formular.html", {"form": form})

# Potvrzovací stránka
def poptavka_odeslana(request):
    return render(request, "poptavky/odeslano.html")
