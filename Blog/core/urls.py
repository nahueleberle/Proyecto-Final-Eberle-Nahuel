"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', mostrar_productos, name='products'),
    path('logout/', exit, name='exit'),
    path('login/', login_request, name = 'login'),
    path('register/', register, name = 'register'),
    path('avatar/', agregar_avatar, name= "agregar_avatar"),
    path('accounts/profile/', profile, name= "perfil"),
    path('accounts/editarperfil/', editarPerfil, name="editarperfil"),
    
]
