from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(User):
    age=models.PositiveSmallIntegerField(help_text="Age of customer")
    phone_number=models.IntegerField(unique=True,help_text="Phone Number of customer")
    monthly_income=models.IntegerField(help_text="Monthly income of customer")
