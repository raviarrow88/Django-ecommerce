from django.db import models
from .timestamp import TimeStamp
from django.core.validators import RegexValidator

class Contact(TimeStamp):
    name = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,12}$',
                                 message="Phone number must be entered in the format: '9848281223'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],max_length=10,verbose_name='Phone Number',null=True,blank=True)
    message = models.TextField()


    def __str__(self):
        return "{0}-{1}".format(self.name,self.phone_number)
