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

        items = order.orderitem_set.all()

        cart_value = sum([item.quantity for item in items])


        context = {'items':items,'order':order,'cart_value':cart_value}
    else:
        items=[]
        context={'items':items}
    return render(request,"cart.html",context)


from baseapp.models.address import Address

def checkout(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        res = get_cart_value(user_id)
        profile = UserProfile.objects.get(user__id=user_id)

        address = Address.objects.filter(user=profile)


        context = {'address':address,'order':res[0],'cart_value':res[1]}

    else:
        context={}
    return render(request,"checkout.html",context)

def store(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        res = get_cart_value(user_id)

        query = request.GET.get('category')
        print (query)
        if query:
            items = Item.objects.filter(category__choices=query)
        else:
            items = Item.objects.all()

        context = {'store_items':items,'cart_value':res[1]}
    else:
        items=[]
        context={'store_items':items,'cart_value':0}


    return render(request,"store.html",context)

def detail(request,id=None):
    res = get_cart_value(request.user.id)
    item_instance= get_object_or_404(Item,id=id)

    context={"item":item_instance,'cart_value':res[1]}
    return render(request,"product_detail.html",context)

def login_cancel(request):
    return redirect("SKART:store")


def get_cart_value(user_id):
    profile = UserProfile.objects.get(user__id=user_id)
    # print (profile)
    order,created = Order.objects.get_or_create(user=profile)

    items = order.orderitem_set.all()

    cart_value = sum([item.quantity for item in items])

    return order,cart_value




@csrf_exempt
def update_cart_items(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        print (data)
        user_id = request.user.id
        profile = UserProfile.objects.get(user__id=user_id)

        order,created = Order.objects.get_or_create(user=profile)

        order_item,created= OrderItem.objects.get_or_create(
        order=order,
        item=Item.objects.get(id=data['product_id']),
        )

        if data['action'] == 'add':
            order_item.quantity +=1
        elif data['action'] == 'remove':
            order_item.quantity -=1

        order_item.save()

        items = order.orderitem_set.all()

        val = sum([item.quantity for item in items])


        if order_item.quantity <= 0:
            order_item.delete()

    return JsonResponse({"message":"Cart Updated SuccessFully","cart_value":val})



from .forms import ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def contact(request):
    res = get_cart_value(request.user.id)
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent SuccessFully')
            return HttpResponseRedirect(reverse('SKART:contact'))
    else:
        form = ContactForm()

    context={'form':form,'cart_value':res[1]}
    return render(request,'contact.html',context)


from django.template.loader import render_to_string

@csrf_exempt
def get_category_data(request):

    cat_type = request.GET.get('category')

    items = Item.objects.filter(category__choices=cat_type)
    data = {
    "data":[i.to_dict() for i in items]
    }

    print (request.path)
    context={'store_items':items}
    filtered_html = render_to_string('items_list.html',context,request=request)

    return JsonResponse({'fh':filtered_html,'type':cat_type})
