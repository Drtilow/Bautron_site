from django.shortcuts import render

def zasady_ochrany(request):
    return render(request, 'zasady.html')
