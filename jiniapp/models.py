from django.db import models

# Create your models here.
class catogorydb(models.Model):
    Catogory_name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to='catogory_image',null=True,blank=True)
class productdb(models.Model):
    Catogory_name = models.CharField(max_length=100, null=True, blank=True)
    Product_name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Image = models.ImageField( upload_to= 'product_image' ,null=True,blank=True)
class Contact(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)