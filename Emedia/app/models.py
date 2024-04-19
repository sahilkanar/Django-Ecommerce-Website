from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class Products(models.Model):
    title=models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image=models.ImageField(upload_to='media/')
    price=models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Products,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.cart

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.rating

Status_choice=(
    ('APPROVED','APPROVED'),
    ('DELIVERD','DELIVERD')
)
class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    status = models.CharField(max_length=100,choices=Status_choice,default='pending')
    total_amount=models.IntegerField()
    fname=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)


    def __str__(self) -> str:
        return self.product
