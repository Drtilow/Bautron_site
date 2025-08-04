from django.contrib import admin
from django.urls import path, include
from uzivatele.views import zasady_ochrany, o_nas 
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poptavky/', include('poptavky.urls')),
    path('reference/', include('reference.urls')),
    path('ucet/', include('uzivatele.urls')),

]

# Připojení media souborů (pokud používáš MEDIA_URL)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    path('', lambda request: redirect('seznam_poptavek', permanent=False)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
