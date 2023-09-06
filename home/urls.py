from django.contrib import admin
from django.urls import path
from home import views

urlpatterns =[
    path("", views.index, name='home'),
    
    path("PatientHome/", views.PatientHome, name="PatientHome"),
    

    path("DoctorHome/", views.DoctorHome, name="DoctorHome"),

    path("Patient_login", views.Patient_login, name="Patient_login"),
    path("Patient_logout/", views.Patient_logout, name="Patient_logout"),

    path("Patient_signup/", views.Patient_signup, name="Patient_signup"),

    path("Doctor_login", views.Doctor_login, name="Doctor_login"),
    path("Doctor_logout/", views.Doctor_logout, name="Doctor_logout"),

    path("Doctor_signup/", views.Doctor_signup, name="Doctor_signup"),
    
    
    
]