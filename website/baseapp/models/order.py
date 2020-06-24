from django.db import models

from .timestamp import TimeStamp
# from .user import UserProfile
from customer.models import UserProfile
from .item import Item

class Order(TimeStamp):
    user =models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
