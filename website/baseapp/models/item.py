from django.db import models

from .timestamp import TimeStamp
from baseapp.helpers.choices import CATEGORY_CHOICES

class Item(TimeStamp):
    name = models.CharField(max_length=255,null=True,blank=True)
    price = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    category = models.CharField(max_length=20,choices= CATEGORY_CHOICES,default='ELECTRONICS')
    description = models.TextField(null=True,blank=False)
    slug = models.SlugField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return str(self.id)


class ProductImage(TimeStamp):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    image = models.ImageField()
    name= models.CharField(max_length=255)

    def __str__(self):
        return str(self.item.id)+'-'+str(self.name)
