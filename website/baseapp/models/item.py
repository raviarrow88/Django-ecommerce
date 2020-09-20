from django.db import models

from .timestamp import TimeStamp
from baseapp.helpers.choices import CATEGORY_CHOICES
from django.template.defaultfilters import slugify

class Category(TimeStamp):
    choices = models.CharField(max_length=20,choices= CATEGORY_CHOICES,default='ELECTRONICS')

    def __str__(self):
        return str(self.choices)



class Item(TimeStamp):
    name = models.CharField(max_length=255,null=True,blank=True)
    price = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
    description = models.TextField(null=True,blank=False)
    slug = models.SlugField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return str(self.id)

    def to_dict(self):
        data = {
        "id":self.id,
        "name":self.name,
        "price":self.price,
        "category": self.category.choices if self.category else None,
        "description":self.description,
        "images":[ i.image.url for i in self.productimage_set.all() ]
        }
        return data

    def imageUrl(self):
        return self.productimage_set.all()[0].image.url


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProductImage(TimeStamp):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    image = models.ImageField()
    name= models.CharField(max_length=255)

    def __str__(self):
        return str(self.item.id)+'-'+str(self.name)
