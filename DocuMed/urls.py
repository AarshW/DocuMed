"""
URL configuration for DocuMed project.

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
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.contrib.auth import views as auth_views 
from doctors import views as doctor_views
from patients import views as patient_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docreg/',doctor_views.RegisterDoc,name = 'RegisterDoc'),
    path('patreg/',patient_views.RegisterPatient,name = 'RegisterPatient'),
    path('redirect/', doctor_views.redirect_user, name='redirect_user'),
    #path('redirectpat/', patient_views.redirect_user, name='redirect_pat'),
    path('logindoc/',auth_views.LoginView.as_view(template_name='doctors/Login.html'),name = 'Doclogin'),
    path('loginpat/',auth_views.LoginView.as_view(template_name='patients/Login.html'),name = 'patlogin'),
    path('patient/', include('patients.urls')),
    path('doctor/', include('doctors.urls')),
    path('', home, name='home'),
]
