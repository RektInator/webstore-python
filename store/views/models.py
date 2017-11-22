from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=128)
    streetnumber = models.IntegerField()
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=64)

class Accounts(models.Model):
    GENDERS = (
        ("m", "Male"),
        ("f", "Female"),
        ("r", "Retarded"),
    )
    fullname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    billingaddress = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    shippingaddress = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    administrator = models.BooleanField(default=False)

class Image(models.Model):
    caption = models.CharField(max_length=64, blank=True)
    # blob = models.BinaryField(max_length=16777216)
    url = models.URLField()

class Products(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

class ProductImages(models.Model):
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()

class ProductCategories(models.Model):
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

class Orders(models.Model):
    customer = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()

class Wishlist(models.Model):
    customer = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)

class Shoppingcart(models.Model):
    customer = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
