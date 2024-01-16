from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Custom phone number validator
telephone_validator = RegexValidator(
    regex=r'^\d{10,15}$',
    message='Enter a valid phone number.',
)


# A new profile is created when User signs up using signals.py
class Profile(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    address1        = models.CharField(max_length=250)
    address2        = models.CharField(max_length=250,blank=True)
    post_code       = models.CharField(max_length=250)
    city            = models.CharField(max_length=250)
    country         = CountryField()
    email           = models.EmailField(max_length=250)
    telephone       = models.CharField(max_length=20, validators=[telephone_validator])
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_on       = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username
