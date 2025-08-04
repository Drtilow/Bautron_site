from django.urls import path
from . import views

urlpatterns = [
    path('', views.reference_list, name='reference_list'),
]
