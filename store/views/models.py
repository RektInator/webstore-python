from django.db import models

# Create your models here.
class Accounts(models.Model):
    GENDERS = (
        ("m", "Male"),
        ("f", "Female"),
        ("r", "Retarded"),
    )
    fullname = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=128)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
