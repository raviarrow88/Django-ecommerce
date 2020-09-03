from django.db import models
from .timestamp import TimeStamp
from .item import Item
# from .user import UserProfile
from customer.models import UserProfile
from baseapp.helpers.choices import ADDRESS_TYPE
from .order import Order

class Address(TimeStamp):
    title = models.CharField(max_length=255,unique=True)
    user = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=False)
    street_address = models.CharField(max_length=250,null=False,blank=False,verbose_name='Address1')
    apartment_address = models.CharField(max_length=250,null=False,blank=False,verbose_name='Address2')
    zip = models.CharField(max_length=6,null=False,blank=False)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE)
    state=models.CharField(max_length=255,blank=False)
    city=models.CharField(max_length=255,blank=False)

    def __str__(self):
        return self.street_address

    class Meta:
        verbose_name_plural = 'Addresses'
