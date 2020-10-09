from django.db import models
from .timestamp import TimeStamp
from .item import Item
# from .user import UserProfile
from customer.models import UserProfile
from baseapp.helpers.choices import ADDRESS_TYPE
from .order import Order
from django.core.validators import RegexValidator

class Address(TimeStamp):
    user = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=False)
    street_address = models.CharField(max_length=250,null=False,blank=False,verbose_name='Address1')
    apartment_address = models.CharField(max_length=250,null=False,blank=False,verbose_name='Address2')
    zip = models.CharField(max_length=6,null=False,blank=False)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE)
    state=models.CharField(max_length=255,blank=False)
    city=models.CharField(max_length=255,blank=False)
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,12}$',
                                 message="Phone number must be entered in the format: '9848281223'. Up to 11 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex],max_length=10,verbose_name='Phone Number',null=False,blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Addresses'
