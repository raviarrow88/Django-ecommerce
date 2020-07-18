
from django.urls import path
from .views import cart,checkout,store,detail,update_cart_items


urlpatterns = [
# path('',login,name='login'),
path('',store,name='store'),
path('cart/',cart,name='cart'),
path('checkout/',checkout,name='checkout'),
path('detail/<int:id>/',detail,name='detail'),
path('update_cart/',update_cart_items,name='update-cart-items')

]
