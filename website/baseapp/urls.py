
from django.urls import path
from .views import cart,checkout,store,detail,update_cart_items,contact,get_category_data,create_address
from .payment_views import stripeConfig,createCheckoutSession,paymentSuccess,paymentCancelled

urlpatterns = [
# path('',login,name='login'),
path('',store,name='store'),
path('cart/',cart,name='cart'),
path('checkout/',checkout,name='checkout'),
path('detail/<slug:slug>/',detail,name='detail'),
path('update_cart/',update_cart_items,name='update-cart-items'),
path('contact/',contact,name='contact'),
path('category/',get_category_data,name='get_category_data'),
path('create_address_api/',create_address,name='create_address_api'),

#payment URLs

path('config/',stripeConfig),
path('create_checkout_session/',createCheckoutSession),
path('success/',paymentSuccess),
path('cancelled/',paymentCancelled)


]
