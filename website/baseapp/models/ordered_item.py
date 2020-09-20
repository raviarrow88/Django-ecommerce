from django.db import models
from .timestamp import TimeStamp
from .item import Item
# from .user import UserProfile
from .order import Order

class OrderItem(TimeStamp):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    @property
    def total_value(self):
        return self.quantity * self.item.price

    @property
    def get_quantity(self):
        return self.quantity
