from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# REGISTRACE
def registrace_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'uzivatele/registrace.html', {'form': form})

# PŘIHLÁŠENÍ
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('seznam_poptavek')  # místo 'home'
    else:
        form = AuthenticationForm()
    return render(request, 'uzivatele/login.html', {'form': form})

# ODHLÁŠENÍ
def logout_view(request):
    logout(request)
    return redirect('seznam_poptavek')  # místo 'home'

# STATICKÉ STRÁNKY
def zasady_ochrany(request):
    return render(request, "zasady.html")

def o_nas(request):
    return render(request, "onas.html")
