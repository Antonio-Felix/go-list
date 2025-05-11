from django.contrib import admin
from django.urls import path
from usuarios import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')), 
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('painel/', views.painel_view, name='painel'),
]

