from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
    ValidationError,
    re,
)
from django.db import models

# validators
def validate_favwebsite(url: str) -> None:
    patter = re.compile(r"^(http|https)\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$") 
    if not re.fullmatch(patter,url):
        raise ValidationError("Invalid URL!: www.google.com")


# Create your models here.
class UserRegistration(models.Model):
    username = models.CharField(max_length=15,verbose_name="User Name",validators=[MinLengthValidator(5, message="nome tem q ter pelo menos 5 caracteres")])
    password = models.CharField(max_length=15,verbose_name="Password",validators=[MinLengthValidator(5)])
    confirm_password = models.CharField(max_length=15,verbose_name="Confirm Password",validators=[MinLengthValidator(5)])
    gender = models.CharField(max_length=10,verbose_name="Gender")
    country = models.CharField(max_length=20,verbose_name="Country")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(verbose_name="E-mail")
    postal_code = models.IntegerField(verbose_name="Postal Code",validators=[MinValueValidator(1000), MaxValueValidator(9999999)])
    phone_number = models.CharField(max_length=13,verbose_name="Phone Number")
    profile = models.TextField(verbose_name="Profile of User", blank=True)
    website_url = models.URLField(verbose_name="Website Url")
    terms_conditions = models.BooleanField(verbose_name="Terms & Conditions")
    favwebsite_url = models.CharField(max_length=256, validators=[validate_favwebsite])

