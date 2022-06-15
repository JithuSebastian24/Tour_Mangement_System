from django.db import models

# Create your models here.
class package(models.Model):
    pname=models.CharField(max_length=75)
    pimg=models.ImageField(upload_to='pic')
    pdays=models.CharField(max_length=15)
    pdesc=models.CharField(max_length=600)
    pprice=models.FloatField()
    pcat=models.CharField(max_length=20)

class booking(models.Model):
    bname=models.CharField(max_length=20)
    bemail=models.EmailField(max_length=70)
    bphoneno=models.IntegerField()
    bpersonsno=models.IntegerField()
    bcat=models.CharField(max_length=20)
    bpackname=models.CharField(max_length=75)
    bdays=models.CharField(max_length=15)
    btotalprice=models.FloatField()

class Msg(models.Model):
    uname=models.CharField(max_length=20)
    uemail=models.EmailField(max_length=80)
    umsg=models.CharField(max_length=600)
  