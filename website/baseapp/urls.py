
from django.urls import path
from .views import login,cart,checkout,store

urlpatterns = [
path('',login,name='login'),
path('store/',store,name='store'),
path('cart/',cart,name='cart'),
path('checkout/',checkout,name='checkout')

]
