from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Patients
from .models import Patients 
from firebase_admin import db

import firebase_admin
from firebase_admin import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is the HomePage For the Text conversion")

from django.shortcuts import render
from datetime import datetime
from home.models import Patients

@login_required(login_url='Patient_login')
def PatientHome(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        describe = request.POST.get('problem')

        # Create an instance of the PatientHome model and save it
        patient_details = Patients(name=name, email=email, sex=sex, age=age, contact=contact, address=address, describe=describe, date=datetime.today())
        patient_details.save()

    return render(request, 'patientHome.html')  # Replace with the actual template name



@login_required(login_url='Doctor_login')
def DoctorHome(request):
       patient_list=Patients.objects.all()
       return render(request, "DoctorHome.html", {"Patients":patient_list})

    #return render(request,"DoctorHome.html")

def Doctor_login(request):
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request,username=username,password=pass1)
            if user is not None:
              login(request,user)
              return redirect('DoctorHome')
            else:
              return HttpResponse("Username or Password is Incorrect !!!!")
            
        return render(request,"Doctor's login.html", {'user_type': 'patient'})

def Doctor_logout(request):
    logout(request)
    return redirect('Doctor_login')

@csrf_exempt    
def Doctor_signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
             return HttpResponse("Password Mismached")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Doctor_login')
     
    return render(request,"Patient's signup.html", {'user_type': 'doctor'})


def Patient_login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         pass1=request.POST.get('pass')
         users=authenticate(request,username=username,password=pass1)
         if users is not None:
              login(request,users)
              return redirect('PatientHome')
         else:
              return HttpResponse("Username or Password is Incorrect !!!!")
             
    return render(request,"Patient's login.html")

def Patient_logout(request):
    logout(request)
    return redirect('Patient_login')



# Check if Firebase Admin SDK is not already initialized
if not firebase_admin._apps:
    firebase_database_url = 'https://virtucare-be344-default-rtdb.firebaseio.com/Patient'  # Replace with your Firebase Database URL
    firebase_admin.initialize_app()
    firebase_db = db.reference(app=firebase_admin.get_app(), url=firebase_database_url)

@csrf_exempt
def Patient_signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Password Mismatched")

        try:
            Patient = auth.create_user(email=email, password=pass1)
            # Add user data to the Firebase Database
            Patient_data = {
                'username': uname,
                'email': email,
                # You can include additional user data here
                # Add more fields as needed
            }
            user_ref = firebase_db.child('Patient').child(Patient.uid)
            user_ref.set(Patient_data)
            print(request.body)

            return render(request, "Patient's login.html")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # If the request method is not POST, return a default response
    return render(request,"Patient's signup.html")

































# Initialize Firebase Realtime Database
firebase_database_url = 'https://virtucare-be344-default-rtdb.firebaseio.com/'  # Replace with your Firebase Database URL
firebase_db = db.reference(app=firebase_admin.get_app(), url=firebase_database_url)








