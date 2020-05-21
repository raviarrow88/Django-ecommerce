from django.db import models
from .timestamp import TimeStamp
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfile(TimeStamp):
    """
    This model is an extension of the User model that is inbuilt in django.
    It is connected to django User model with a OneToOneField.
    """
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    avatar = models.URLField(max_length=100,blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,12}$',
                                 message="Phone number must be entered in the format: '9848281223'. Up to 11 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex],max_length=10,verbose_name='User phone number',null=True,blank=True)

    fb_profile = models.URLField(max_length=255,null=True,blank=True,default=None)
    gmail_profile = models.URLField(max_length=255,null=True,blank=True,default=None)

    def __str__(self):
        return str(self.user)
