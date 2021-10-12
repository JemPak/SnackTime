"""snackWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apps.back import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orden/', views.OrdenListCreateView.as_view()),
    path('orden/<int:pk>', views.ordenView.OrdenRetrieveUpdateDestroy.as_view()),
    path('cliente/', views.ClienteListCreateView.as_view()),
    path('cliente/<int:pk>', views.ClienteRetrieveUpdateDestroy.as_view()),
    path('producto/', views.ProductoListCreateView.as_view()),
    path('producto/<int:pk>', views.ProductoRetrieveUpdateDestroy.as_view()),
    path('maquina/', views.MaquinaListCreateView.as_view()),
    path('maquina/<int:pk>', views.MaquinaRetrieveUpdateDestroy.as_view()),
    path('contacto/', views.ContactoListCreateView.as_view()),
    path('contacto/<int:pk>', views.ContactoRetrieveUpdateDestroy.as_view()),
]
