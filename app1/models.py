from django.db import models

# Create your models here.

class Userregister(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=12)
    # def __str__(self):
    #     return self.name

class Category(models.Model):
    categoryname=models.CharField(max_length=250)
    image=models.ImageField(upload_to="categoryimg")
    def __str__(self):
        return self.categoryname
    
class Product(models.Model):
    vendorid=models.CharField(max_length=250,default="")
    categoryname=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    discription=models.CharField(max_length=200)
    image=models.ImageField(upload_to="productimg")
    quantity=models.IntegerField()

class sellerregister(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=12)


class Cart(models.Model):
    orderid=models.CharField(max_length=250,default="0")
    userid=models.CharField(max_length=250)
    productid=models.CharField(max_length=250)
    vendorid=models.CharField(max_length=250)
    quantity=models.CharField(max_length=250)
    totalprice=models.CharField(max_length=250)

class Order(models.Model):
    userid=models.CharField(max_length=250,default="")
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    number=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    paymentmethod=models.CharField(max_length=250)
    transactionid=models.CharField(max_length=250)
    datetime=models.DateTimeField(auto_created=True,auto_now=True)