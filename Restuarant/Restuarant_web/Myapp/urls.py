from django.urls import path
from Myapp import views

urlpatterns = [

    #signin and up
    
    path('signin', views.signin , name='signin'),

    path('signup', views.signup , name='signup'),

    #Logout path

    path('logout', views.logouts, name='logout'),

    #tempolate
    path('',views.temp,name='index'),

    path('customers',views.savecustomer,name='customer'),

    path('updatecustomer/<str:pk>',views.updatecustomer,name='updatecustomer'),

    path('deletecustomer/<str:pk>',views.deletecustomer,name='deletecustomer'),

    #cart data--------------------------------
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),

    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),

    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),

    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),

    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),

    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    #cart buy---------------------------------
    path('store', views.store, name='store'),
]