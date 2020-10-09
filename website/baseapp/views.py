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
import json,stripe
from decimal import Decimal
from baseapp.helpers.utils import get_cart_value,create_cart,get_cookie_cart_quantity
from django.conf import settings

def cart(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        profile = UserProfile.objects.get(user__id=user_id)
        # print (profile)
        order,created = Order.objects.get_or_create(user=profile)

        items = order.orderitem_set.all()



        cart_value = sum([item.quantity for item in order.orderitem_set.all()])

        # context = {'items':items,'order':order,'cart_value':cart_value}
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart={}
        items=[]
        order = {'get_no_items':0,'get_total_order_price':0,'get_cart_total':0,"get_delivery_fee":0}
        for i in cart:
            order['get_no_items'] += cart[i]['quantity']
            item = Item.objects.get(id=i)
            order['get_total_order_price'] = order['get_no_items'] *  item.price
            item = {
            'item':{
            'id':item.id,
            'price':item.price,
            'name':item.name,

            'imageUrl': item.productimage_set.all()[0].image.url
            },
            'quantity':cart[i]['quantity'],
            }

            print (item)
            items.append(item)

        cart_value = order['get_no_items']
        if int (order['get_total_order_price']) > 500:
            order['get_delivery_fee'] = 0
        else:
            order['get_delivery_fee'] = 500

            order['get_cart_total'] = (order['get_total_order_price']) + Decimal(order['get_delivery_fee'])


    context={'items':items,'order':order,'cart_value':cart_value}
    return render(request,"cart.html",context)


from baseapp.models.address import Address
from .forms import AddressForm

def checkout(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        res = get_cart_value(user_id)
        profile = UserProfile.objects.get(user__id=user_id)

        address = Address.objects.filter(user=profile)

        initail_dict={'email':request.user.email,'id':profile.id}

        if request.method =='POST':
            form = AddressForm(request.POST or None,initial=initail_dict)
            if form.is_valid():
                k = form.save(commit=False)
                k.user = profile
                k.order = res[0]
                k.save()

                stripe.api_key= settings.STRIPE_SECRET_KEY
                Customer = stripe.Customer.modify(
                profile.stripe_id,
                address={
                "city":k.city,
                "country":"IN",
                "line1":k.street_address,
                "line2":k.apartment_address,
                "postal_code":k.zip,
                "state":k.state
                }
                
                )

                return HttpResponseRedirect(reverse('SKART:checkout'))

        else:
            form = AddressForm(initial=initail_dict)


        context = {'address':address,'order':res[0],'cart_value':res[1],'form':form}

    else:
        form = AddressForm()
        try:
            cart=json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        order = {'get_no_items':0,'get_total_order_price':0,'get_cart_total':0,"get_delivery_fee":0}
        for i in cart:
            order['get_no_items'] += cart[i]['quantity']
            item = Item.objects.get(id=i)
            order['get_total_order_price'] = order['get_no_items'] *  item.price

        cart_value = order['get_no_items']
        if int (order['get_total_order_price']) > 500:
            order['get_delivery_fee'] = 0
        else:
            order['get_delivery_fee'] = 500

            order['get_cart_total'] = (order['get_total_order_price']) + Decimal(order['get_delivery_fee'])

        context={'form':form,'order':order,'cart_value':cart_value,'address':None}
        print (context)
    return render(request,"checkout.html",context)





def store(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart={}
    if request.user.is_authenticated:

        if bool(cart):
            context = create_cart(request,cart)
            response = render(request,'cart.html',context)
            response.delete_cookie('cart')
            return response


        user_id = request.user.id
        res = get_cart_value(user_id)
        query = request.GET.get('category')

        if query:
            items = Item.objects.filter(category__choices=query)
        else:
            items = Item.objects.all()

        quantity = res[1]
        # context = {'store_items':items,'cart_value':res[1]}
    else:
        items = Item.objects.all()

        quantity = get_cookie_cart_quantity(cart)


    context={'store_items':items,'cart_value':quantity}
    return render(request,"store.html",context)

def detail(request,slug=None):
    item_instance= get_object_or_404(Item,slug=slug)
    if request.user.is_authenticated:
        res = get_cart_value(request.user.id)
        quantity = res[1]
    else:
        try:
            cart=json.loads(request.COOKIES['cart'])
        except:
            cart={}
        quantity = get_cookie_cart_quantity(cart)


    context={"item":item_instance,'cart_value':quantity}
    return render(request,"product_detail.html",context)

def login_cancel(request):
    return redirect("SKART:store")







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
    if request.user.is_authenticated:
        res = get_cart_value(request.user.id)
        if request.method=='POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Message Sent SuccessFully')
                return HttpResponseRedirect(reverse('SKART:contact'))
        else:
            form = ContactForm()
        quantity = res[1]
    else:
        form=ContactForm()
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart={}
        quantity = get_cookie_cart_quantity(cart)


    context={'form':form,'cart_value':quantity}
    return render(request,'contact.html',context)


from django.template.loader import render_to_string

@csrf_exempt
def get_category_data(request):

    cat_type = request.GET.get('category')

    print(request.path)

    items = Item.objects.filter(category__choices=cat_type)
    data = {
    "data":[i.to_dict() for i in items]
    }

    context={'store_items':items}
    filtered_html = render_to_string('items_list.html',context,request=request)

    return JsonResponse({'fh':filtered_html,'type':cat_type})





from django.core.exceptions import ValidationError,FieldError,FieldDoesNotExist
from django.db import IntegrityError

def create_address(request):
    if request.method == 'POST' or request.is_ajax():
        try:
            print (request.body.decode('utf-8'))

            if request.POST['title']=='':
                print ("No")


            auth_user  = UserProfile.objects.get(user_id=request.user.id)
            address = Address.objects.create(
            title=request.POST.get('title'),
            user= auth_user,
            street_address = request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip = request.POST.get('zipcode')
            )
            address.save()
            return JsonResponse({"message":"Added SuccessFully"},status=200)

        except ValidationError as e:
            print ("v",e)
            return JsonResponse({'Error':str(e)},status=404)

        except FieldError as e:
            print("F",e)
            return JsonResponse({'Error':str(e)},status=404)
        except IntegrityError as e:
            print ('I',e.args,e)
            if 'UNIQUE constraint' in e.args[0]:
                return JsonResponse({'Error':"Title already exists"},status=404)
        except Exception as e:
            print ('Ex',e)
            return JsonResponse({'Error':str(e)},status=404)



from .documents import ItemDocument

def search(request):
    q = request.GET.get('q')
    print (q)
    if q:
        items = ItemDocument.search().filter("term",name=q)
    else:
        items = ''


    context={"store_items":items}

    return render(request,"store.html",context)
