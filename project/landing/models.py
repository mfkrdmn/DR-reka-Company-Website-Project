from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    namesurname = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    mobile_phone = models.CharField(max_length=15, blank=True)
    web_site = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True,null=True)
    image  = models.ImageField(upload_to='profil_foto/',blank = True,null = True)

    def __str__(self) :
        return self.user.username


class rfq(models.Model):
    PartNumber = models.CharField(max_length=50, blank=True)
    Description = models.CharField(max_length=150, blank=True)
    Quantity = models.CharField(max_length=50, blank=True)
    Condition = models.CharField(max_length=50, blank=True)
    Mail = models.CharField(max_length=50, blank=True)
    Telephone = models.CharField(max_length=50, blank=True)
    CompanyName = models.CharField(max_length=50, blank=True)
    fullname = models.CharField(max_length=50, blank=True)


    def __str__(self) :
        return self.Description

class urun(models.Model):
    isim_tr = models.CharField(verbose_name="İsim Türkçe" , max_length=200)
    isim_en = models.CharField(verbose_name="İsim inglizce" , max_length=200)
    isim_de = models.CharField(verbose_name="İsim almanca" , max_length=200)
    isim_ar = models.CharField(verbose_name="İsim arapca" , max_length=200)
    image  = models.ImageField(upload_to='gsefoto/',blank = True,null = True,verbose_name="Size Ait Olan Resmi Ekleyin")

    def __str__(self) :
        return self.isim_en

class all_product(models.Model):
    pn = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    ac_type = models.CharField(max_length=200)
    qty = models.BigIntegerField()
    price = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.ac_type