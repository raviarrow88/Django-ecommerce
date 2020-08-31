from django.db import models
from .timestamp import TimeStamp
from .item import Item
# from .user import UserProfile
from customer.models import UserProfile
from baseapp.helpers.choices import ADDRESS_TYPE
from .order import Order

class Address(TimeStamp):
    title = models.CharField(max_length=255,unique=True)
    user = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    street_address = models.CharField(max_length=250,null=False)
    apartment_address = models.CharField(max_length=250,null=False)
    zip = models.CharField(max_length=6,null=False)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE)

    def __str__(self):
        return self.street_address

    class Meta:
        verbose_name_plural = 'Addresses'
