from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from poptavky import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("poptavky/", include("poptavky.urls")),
    path("", lambda request: redirect("seznam_poptavek", permanent=False)),  # přesměrování na /poptavky/
    path('ucet/', include('uzivatele.urls')),
    path('reference/', include('reference.urls')),
    path('obestaveny_prostor/', views.obestaveny_prostor, name='obestaveny_prostor'),


]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poptavky/', include('poptavky.urls')),
    path('reference/', include('reference.urls')),
    path('ucet/', include('uzivatele.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poptavky/', include('poptavky.urls')),
    path('reference/', include('reference.urls')),
    path('ucet/', include('uzivatele.urls')),

    # Přesměrování / na seznam poptávek (nebo jinam, dle potřeby)
    path('', lambda request: redirect('seznam_poptavek', permanent=False)),
]

