from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)

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