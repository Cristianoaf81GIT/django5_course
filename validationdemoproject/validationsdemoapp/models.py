from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    username = models.CharField(max_length=15,verbose_name="User Name")
    password = models.CharField(max_length=15,verbose_name="Password")
    confirm_password = models.CharField(max_length=15,verbose_name="Confirm Password")
    gender = models.CharField(max_length=10,verbose_name="Gender")
    country = models.CharField(max_length=20,verbose_name="Country")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(verbose_name="E-mail")
    postal_code = models.IntegerField(verbose_name="Postal Code")
    phone_number = models.CharField(max_length=13,verbose_name="Phone Number")
    profile = models.TextField(verbose_name="Profile of User", blank=True)
    website_url = models.URLField(verbose_name="Website Url")
    terms_conditions = models.BooleanField(verbose_name="Terms & Conditions")
    favwebsite_url = models.CharField(max_length=256)

