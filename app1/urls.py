
from django.urls import path
from app1.views import *

urlpatterns = [
    path('data/',data),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout1"),
    path('profile/',profile,name="profile12"),
    path('register/',register,name="register"),
    path('',index,name="index"),
    path('all-product/',allproduct,name="proall"),
    path('filter-product/<int:id>/',filterproduct,name="productfilter"),
    path('product-get/<int:id>/',productget,name="proget1"),
    path('seller-Register/',Sellerregister,name="sregister"),
    path('seller-Login/',sellerlogin,name="slogin"),
    path('seller-Logout/',sellerlogout,name="slogout"),
    path('Add-Product/',addproduct,name="addproduct1"),
    path('Add-cart/',addcart,name="cart"),
    path('viewcart/',viewcart,name="view_cart"),
    path('removeitem/<int:id>/',removeitem,name="itemremove"),
    path('remove-allitem/',removeallitem,name="remove_allitem"),
    path('shipping/',shipping,name="shipp"),
    path('success/',success,name="success123"),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('order-table/',ordertable,name="order123")
]