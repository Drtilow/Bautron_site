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
