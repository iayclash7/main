from django.db import models

# Create your models here.


class product_info1(models.Model):
    objects=None
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField()
    product_des=models.CharField(max_length=30)
    product_contact=models.IntegerField()
    product_image=models.ImageField(upload_to='pics')


class userregistration1(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    retype_password=models.CharField(max_length=30)
    email=models.EmailField()
