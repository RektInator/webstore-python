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
    billingaddress = models.ForeignKey(Address, null=True, on_delete=models.CASCADE, related_name="billingaddr")
    shippingaddress = models.ForeignKey(Address, null=True, on_delete=models.CASCADE, related_name="shippingaddr")
    administrator = models.BooleanField(default=False)

class Image(models.Model):
    caption = models.CharField(max_length=64, blank=True)
    url = models.URLField()

class Products(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

class Filters(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)

class ProductFilters(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filters, on_delete=models.CASCADE)

class ProductSize(models.Model):
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    price = models.FloatField(default=0)
    name = models.CharField(max_length=128, default="")

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
    STATUS = (
        ("In Process", "In Process"),
        ("Paid", "Paid"),
        ("Shipped", "Shipped"),
        ("Complete", "Complete"),
    )
    customer = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField(default=0)
    status = models.CharField(max_length=32, choices=STATUS, default="In Process")

class Wishlist(models.Model):
    customer = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)

class Shoppingcart(models.Model):
    customer = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductSize, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, null=True, default=None, on_delete=models.CASCADE)
