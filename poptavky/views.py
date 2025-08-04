from django.shortcuts import render, redirect
from .forms import PoptavkaForm

def formular_poptavky(request):
    if request.method == 'POST':
        form = PoptavkaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'poptavky/dekujeme.html')
    else:
        form = PoptavkaForm()

    return render(request, 'poptavky/formular.html', {'form': form})
from .models import Poptavka

from django.contrib.auth.decorators import login_required

@login_required
def seznam_poptavek(request):
    poptavky = Poptavka.objects.all().order_by('-odeslano')
    return render(request, 'poptavky/seznam.html', {'poptavky': poptavky})
def obestaveny_prostor(request):
    objem = None
    if request.method == "POST":
        sirka = float(request.POST.get("sirka", 0))
        delka = float(request.POST.get("delka", 0))
        vyska = float(request.POST.get("vyska", 0))
        objem = round(sirka * delka * vyska, 2)
    return render(request, 'poptavky/obestaveny_prostor.html', {"objem": objem})
def o_nas(request):
    return render(request, 'poptavky/o_nas.html')