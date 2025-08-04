from django.shortcuts import render
from .models import Reference

def reference_list(request):
    reference = Reference.objects.all().order_by('-datum_realizace')
    return render(request, 'reference/reference_list.html', {'reference': reference})
