# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Totems(models.Model):

    #__Totems_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    anydeskid = models.CharField(max_length=255, null=True, blank=True)
    anydeskpassword = models.CharField(max_length=255, null=True, blank=True)
    postalcode = models.CharField(max_length=255, null=True, blank=True)

    #__Totems_FIELDS__END

    class Meta:
        verbose_name        = _("Totems")
        verbose_name_plural = _("Totems")


class Users(models.Model):

    #__Users_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Categories(models.Model):

    #__Categories_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)

    #__Categories_FIELDS__END

    class Meta:
        verbose_name        = _("Categories")
        verbose_name_plural = _("Categories")



#__MODELS__END
