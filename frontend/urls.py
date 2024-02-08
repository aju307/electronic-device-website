from django.urls import path
from frontend import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('single_product/<int:pdtid>',views.single_product,name='single_product'),
    path('product_filters/<catname>',views.product_filters,name='product_filters'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contactus/',views.contactus,name='contactus'),
    path('contactdata/',views.contactdata,name='contactdata'),
    path('Reg/',views.Reg,name='Reg'),
    path('regdata/',views.regdata,name='regdata'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logout/', views.logout, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('savecart/', views.savecart, name="savecart"),
    path('deletecart/<int:pro_id>/', views.deletecart, name="deletecart"),
    path('checkout/', views.checkout, name="checkout"),


]