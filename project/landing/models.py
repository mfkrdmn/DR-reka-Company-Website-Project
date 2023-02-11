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