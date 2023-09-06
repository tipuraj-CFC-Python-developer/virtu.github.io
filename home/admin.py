from django.contrib import admin
from home.models import Patients



class Patientadmin(admin.ModelAdmin):
    list_display= ["name","email","sex","age","contact","address","describe","date"]
    search_fields= ["name","date"]
    list_per_page= 20

# Register your models here.
admin.site.register(Patients,Patientadmin)