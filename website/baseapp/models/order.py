from django.db import models

from .timestamp import TimeStamp
# from .user import UserProfile
from customer.models import UserProfile
from .item import Item

class Order(TimeStamp):
    user =models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,blank=True)
    completed = models.BooleanField(default=False)
    delivery_charge = models.IntegerField(default=40,blank=False)
    transaction_id = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_order_price(self):
        order_items = self.orderitem_set.all()
        return sum([item.total_value for item in order_items])

    @property
    def get_no_items(self):
        order_items = self.orderitem_set.all()
        return sum([item.quantity for item in order_items ])

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.total_value for item in order_items])
        if total < 500:
            return total+self.delivery_charge
        else:
            return total

    @property
    def get_delivery_fee(self):
        order_items = self.orderitem_set.all()
        total = sum([item.total_value for item in order_items])
        if total > 500:
            return 0
        else:
            return self.delivery_charge
