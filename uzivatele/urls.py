from django.urls import path
from . import views

urlpatterns = [
    path('registrace/', views.registrace_view, name='registrace'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("zasady/", views.zasady_ochrany, name="zasady"),
    path("o-nas/", views.o_nas, name="o_nas"),
]
