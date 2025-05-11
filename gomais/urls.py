from django.contrib import admin
from django.urls import include, path
from usuarios import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')), 
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('painel/', views.painel_view, name='painel'),
]
# from django.contrib import admin
# from django.urls import path, include
# from usuarios.views import Cadastro, Login, Usuario, Logout
# from django.shortcuts import redirect


# urlpatterns = [
#     path('', lambda request: redirect('login')), 
#     path('admin/', admin.site.urls),
#     path('cadastro/', Cadastro.as_view(), name='cadastro'),
#     path('login/', Login.as_view(), name='login'),
#     path('logout/', Logout.as_view(), name='logout'),
#     path('painel/', Usuario.as_view(), name='painel'),
#     path('', include('usuarios.urls')),
# ]

