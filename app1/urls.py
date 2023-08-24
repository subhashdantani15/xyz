
from django.urls import path
# from app1.views import data,index,productall
from app1.views import *

urlpatterns = [
    path('data/',data),
    path('',index,name="home"),
    path('product-all/',productall,name='productall'),
    path('product-filter/<int:id>/',productfilter,name='product_filter'),
    path('product-get/<int:id>',productget,name="product_get"),
    path('login/',login,name="login1"),
    path('logout/',logout,name='logout1'),
    path('register/',register,name="register1"),
    path('profile/',profile,name="profile1"),
    path('Change-Password/',changepass,name="changepass"),
    path('Vendor-login/',vendorlogin,name="Vendorlogin"),
    path('vendor-register/',vendorregister,name='vendorregister'),
    path('vendor-logout/',vendorlogout,name="vendorlogout"),
    path('add_product/',add_product,name="addproduct"),
    path('success/',success,name="success1"),
    path('update-product/<int:id>/',updateproduct,name="updateproduct1"),
    path('add-cart/',addcart,name="addcart123"),
    path('cart/',cartpage,name="cart2"),
    path('removeitem/<int:id>/',removeitem,name="removeitem"),
    path('removeallitem/',removeallitem,name="removeallitem"),
    path('shiping/',shiping,name="shiping"),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('order-table/',ordertable,name="ordertable"),
    path('order-details/<int:id>/',orderdetails,name="orderdetails2"),
    path('vendor-order/',vendor_order,name="vendor_order"),
    path('search/',productsearch,name="search")

] 