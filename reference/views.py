from django.shortcuts import render
from .models import Reference
from django.shortcuts import render

def reference_list(request):
    reference = Reference.objects.all()
    return render(request, 'reference/reference_list.html', {'reference': reference})
def obestaveny_prostor(request):
    return render(request, 'poptavky/obestaveny_prostor.html')
