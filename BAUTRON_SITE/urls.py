from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("poptavky/", include("poptavky.urls")),
    path("", lambda request: redirect("seznam_poptavek", permanent=False)),  # přesměrování na /poptavky/
    path('ucet/', include('uzivatele.urls')),

]
