from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .models.item import Item
from baseapp.models.order import Order
from baseapp.models.ordered_item import OrderItem
from baseapp.models.item import Item
from customer.models import UserProfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def cart(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        profile = UserProfile.objects.get(user__id=user_id)
        # print (profile)
        order,created = Order.objects.get_or_create(user=profile)
        print(order)
        items = order.orderitem_set.all()
        context = {'items':items,'order':order}
    else:
        items=[]
        context={'items':items}
    return render(request,"cart.html",context)

def checkout(request):

    context={}
    return render(request,"checkout.html",context)

def store(request):
    items = Item.objects.all()
    context={"items":items}
    return render(request,"store.html",context)

def detail(request,id=None):
    item_instance= get_object_or_404(Item,id=id)
    context={"item":item_instance}
    return render(request,"product_detail.html",context)

def login_cancel(request):
    return redirect("SKART:store")

@csrf_exempt
def update_cart_items(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        user_id = request.user.id
        profile = UserProfile.objects.get(user__id=user_id)
        # print (profile)
        order,created = Order.objects.get_or_create(user=profile)

        order_item,created= OrderItem.objects.get_or_create(
        order=order,
        item=Item.objects.get(id=data['product_id']),
        )
        order_item.quantity +=1
        order_item.save()


    return JsonResponse({"message":"Cart Updated SuccessFully"})
