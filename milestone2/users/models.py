# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from django.contrib.auth.validators import UnicodeUsernameValidator

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
