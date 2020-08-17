from django.contrib import admin

# Register your models here.
# from .models.user import UserProfile
from .models.item import Item,ProductImage
from .models.address import Address
from .models.order import Order
from .models.ordered_item import OrderItem

# admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderItem)
admin.site.register(ProductImage)
