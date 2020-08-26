
from django.urls import path
from .views import cart,checkout,store,detail,update_cart_items,contact,get_category_data


urlpatterns = [
# path('',login,name='login'),
path('',store,name='store'),
path('cart/',cart,name='cart'),
path('checkout/',checkout,name='checkout'),
path('detail/<int:id>/',detail,name='detail'),
path('update_cart/',update_cart_items,name='update-cart-items'),
path('contact/',contact,name='contact'),
path('category/',get_category_data,name='get_category_data')
]
