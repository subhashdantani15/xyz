from django.db import models

# Create your models here.

class Userregister(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=12)

    # def __str__(self) -> str:
    #     return self.name

class Category(models.Model):
    categoryname=models.CharField(max_length=200)
    image=models.ImageField(upload_to='category_img',blank=True)
    def __str__(self) -> str:
        return self.categoryname

class Product(models.Model):
    vendorid=models.CharField(max_length=200,default="")
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    img=models.ImageField(upload_to='Product_img')
    quantity=models.IntegerField()
    description=models.TextField()



class Contactus(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    message=models.TextField()

class Vendorregister(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=12)

class Cart(models.Model):
    userid=models.CharField(max_length=200)
    productid=models.CharField(max_length=200)
    vendorid=models.CharField(max_length=200)
    orderid=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    totalprice=models.CharField(max_length=200)

class Order(models.Model):
    userid=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    totalprice=models.CharField(max_length=200)
    paymentmethod=models.CharField(max_length=250)
    transactionid=models.CharField(max_length=250)
    datetime=models.DateTimeField(auto_created=True,auto_now=True)