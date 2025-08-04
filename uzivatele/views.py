from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def registrace_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # nebo 'home'
    else:
        form = UserCreationForm()
    return render(request, 'uzivatele/registrace.html', {'form': form})

from django.shortcuts import render

def zasady_ochrany(request):
    return render(request, "zasady.html")

def o_nas(request):
    return render(request, "onas.html")

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # nebo jiná stránka po přihlášení
    else:
        form = AuthenticationForm()
    return render(request, 'uzivatele/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')  # nebo 'login' – podle tvé volby

