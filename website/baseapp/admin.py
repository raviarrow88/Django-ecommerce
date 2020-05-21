from django.contrib import admin

# Register your models here.
from .models.user import UserProfile
from .models.item import Item


admin.site.register(UserProfile)
admin.site.register(Item)
