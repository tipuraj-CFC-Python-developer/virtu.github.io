from django.db import models

# Create your models here.
class Patients(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    sex=models.CharField(max_length=12)
    age=models.CharField(max_length=3)
    contact=models.CharField(max_length=13)
    address=models.CharField(max_length=300)
    describe=models.TextField(default="", blank=True, null=True)
    date=models.DateField()

# to display the name variable in the Admin page by serial number.
    def __str__(self):
        return self.name
    