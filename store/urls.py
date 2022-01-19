from django.contrib import admin
from django.urls import path
from .views.home import Index , store, home, profile, desc
from .views.signup import Signup
from .views.login import Login , logout
# from .views.cart import Cart, delete_p
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.favorite import Favorite
from .views.cart import processOrder, updateItem

#changed
from .views.cart import cart, checkout
from .views.cart import delete_p
urlpatterns = [
    
    path('', Index.as_view(), name='homepage'),
    path('home', home, name='home'),
    path('store', store , name='store'),
    path('profile', profile, name='profile'),
    path('desc', desc, name='desc'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    # path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('checkout', checkout, name='checkout'),
    
    path('favorite', auth_middleware(Favorite.as_view()) , name='favorite'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    # path('delete_p/<int:pid>', delete_p, name='delete_p'),

    #changed
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    # path('update_shipping/', update_shipping, name='update_shipping'),
    path('cart', cart , name='cart'),
]
