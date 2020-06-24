from django.db import models
from .timestamp import TimeStamp
from .item import Item
# from .user import UserProfile
from .order import Order

class OrderItem(TimeStamp):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
