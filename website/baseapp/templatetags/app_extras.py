from django import template
from baseapp.models.ordered_item import OrderItem

register = template.Library()

@register.filter(name='get_quantity')
def get_quantity(itemId):
    return OrderItem.objects.get(item_id=itemId).quantity
