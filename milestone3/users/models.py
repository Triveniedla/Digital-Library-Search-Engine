# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from django.contrib.auth.validators import UnicodeUsernameValidator
#<!-- user details will be stored in DB using models------------
class User(AbstractUser):
    email_validator = UnicodeUsernameValidator()
    email = models.EmailField(_('email address'),unique=True,blank=False,validators=[email_validator])
    username = models.CharField(_('username'),max_length=150,unique=False,blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class SearchHistoryModel(models.Model):
    searchtext=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    date=models.DateTimeField(auto_now=True)

    contributor_author=models.CharField(max_length=150,blank=True)
    contributor_department=models.CharField(max_length=150,blank=True)
    contributor_committeechair=models.CharField(max_length=150,blank=True)
    description_degree=models.CharField(max_length=150,blank=True)
    date1=models.CharField("1940-01-01",max_length=30,blank=True)
    date2=models.CharField("2020-01-01",max_length=30,blank=True)

    def __str__(self):
        return f"History <{self.user.email}, {self.searchtext}>"

class HandleModel(models.Model):
    handle=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    date=models.DateTimeField(auto_now=True)
