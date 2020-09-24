from baseapp.models.order import Order
from baseapp.models.ordered_item import OrderItem
from baseapp.models.item import Item
from customer.models import UserProfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal




def get_cart_value(user_id):
    profile = UserProfile.objects.get(user__id=user_id)
    # print (profile)
    order,created = Order.objects.get_or_create(user=profile)

    items = order.orderitem_set.all()

    cart_value = sum([item.quantity for item in items])

    return order,cart_value



def create_cart(request,cart):
    # {"1":{"quantity":2},"2":{"quantity":1}}

    profile= UserProfile.objects.get(user__id=request.user.id)
    order,created = Order.objects.get_or_create(user=profile)
    for i in cart:
        item = Item.objects.get(id=i)

        order_item,created = OrderItem.objects.get_or_create(item=item,order=order)
        order_item.quantity += cart[i]['quantity']
        order_item.save()

    items = order.orderitem_set.all()
    cart_value = sum([item.quantity for item in order.orderitem_set.all()])

    context={'items':items,'order':order,'cart_value':cart_value}
    print (context)
    return context
