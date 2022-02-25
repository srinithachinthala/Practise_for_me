from django.db import models

# Create your models here.
class model_for_form(models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.DateField()
    Email_Id=models.EmailField()
    phone_Number=models.IntegerField()
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
   )
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    Flat_no=models.IntegerField()
    street=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    upload_photo=models.ImageField(upload_to="new/")
    


def __str__(self):
    return self.name