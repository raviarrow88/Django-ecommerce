from django.shortcuts import render,redirect

# Create your views here.
from .models.item import Item



def cart(request):
    context={}
    return render(request,"cart.html",context)

def checkout(request):
    context={}
    return render(request,"checkout.html",context)

def store(request):
    items = Item.objects.all()
    context={"items":items}
    return render(request,"store.html",context)

def detail(request):
    context={}
    return render(request,"product_detail.html",context)

def login_cancel(request):
    return redirect("store")
