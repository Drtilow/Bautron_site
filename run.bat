@echo off
REM run.bat – rychlé spuštění Django projektu (cmd)

SETLOCAL ENABLEDELAYEDEXPANSION

REM 1) Kořen projektu = aktuální složka (kde je run.bat)
cd /d "%~dp0"

echo ==> Kontrola virtuálního prostredi...
IF NOT EXIST venv (
    echo     Venv neexistuje, vytvarim...
    py -m venv venv
)

REM 2) Aktivace venv
call venv\Scripts\activate.bat

REM 3) Instalace/aktualizace zavislosti
echo ==> Instalace zavislosti
python -m pip install --upgrade pip
IF EXIST requirements.txt (
    pip install -r requirements.txt
) ELSE (
    pip install "Django==5.2.5" Pillow
)

REM 4) Migrace DB
echo ==> Spoustim migrace
python manage.py migrate

REM 5) (Volitelne) Automaticky superuser (odkomentuj a dopln)
REM set DJANGO_SUPERUSER_USERNAME=admin
REM set DJANGO_SUPERUSER_EMAIL=admin@example.com
REM set DJANGO_SUPERUSER_PASSWORD=admin12345
REM python manage.py createsuperuser --noinput 2>nul

REM 6) Start serveru
echo ==> Spoustim server na http://127.0.0.1:8000
python manage.py runserver

ENDLOCAL
