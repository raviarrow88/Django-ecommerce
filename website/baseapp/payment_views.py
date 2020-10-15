from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from baseapp.models.order import Order
from baseapp.models.ordered_item import OrderItem
from baseapp.models.item import Item
from customer.models import UserProfile
from decimal import Decimal
from django.shortcuts import render
import stripe

@csrf_exempt
def stripeConfig(request):
    if request.method=='GET':

        stripe_config = {'publicKey':settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config,safe=False)




@csrf_exempt
def get_line_items(request):
    profile = UserProfile.objects.get(user__id=request.user.id)
    # print (profile)
    order,created = Order.objects.get_or_create(user=profile)

    items = list(order.orderitem_set.all())


    line_items=[]
    lt= {}
    total = 0

    for item in items:
        lt['name'] = item.item.name
        lt['currency'] = 'inr'
        lt['amount'] = str(int(item.item.price)*100)
        lt['quantity'] = item.quantity
        total += item.item.price
        line_items.append(lt.copy())

    if int(total) < 500:
        total +=40*100
        lt['amount'] = int(total)
        lt['quantity'] = 1
        lt['currency'] ='inr'
        lt['name'] = 'Delivery Fee'
        line_items.append(lt.copy())


    print (items)

    return line_items,str(total)




@csrf_exempt
def createCheckoutSession(request):


    if request.method=='GET':
        domain_url='http://localhost:8000/'
        stripe.api_key= settings.STRIPE_SECRET_KEY

        profile = UserProfile.objects.get(user__id=request.user.id)


        try:
            customer = stripe.Customer.retrieve(profile.stripe_id)
            # print (customer)
            profile = UserProfile.objects.get(user__id=request.user.id)
            checkoutSession = stripe.checkout.Session.create(
            success_url =domain_url+'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url =domain_url+'cancelled/',
            payment_method_types = ['card'],
            mode='payment',
            line_items= get_line_items(request)[0],
            customer= profile.stripe_id,


            )



            return JsonResponse({'sessionId':checkoutSession['id']})


        except Exception as e:
            return JsonResponse({"error":str(e)})



def paymentSuccess(request):
    context={}
    return render(request,'success.html',context)

def paymentCancelled(request):
    context={}
    return render(request,'cancelled.html',context)
