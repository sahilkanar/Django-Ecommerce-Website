from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name='register'),
    path('update/',views.user_update,name='updateprofile'),
    path('product/<int:id>/',views.view_product,name='viewproduct'),
    path('rate/<int:id>/',views.rating,name='rating'),
    path('cart/<int:id>/',views.cart,name='cart'),
    path('search/',views.search,name='data'),
    path('yourcart/',views.viewcart,name='viewcart'),
    path('incart/<int:id>/',views.increase_cart,name='increasecart'),
    path('decart/<int:id>/',views.decrease_cart,name='decreasecart'),
    path('rmcart/<int:id>/',views.remove_cart,name='removecart'),
    path('category/<int:id>/',views.category,name='category'),
    path('search/',views.search,name='search'),
    path('checkout/',views.checkout,name='checkout'),
    path('orders/',views.order,name='orders'),
    

]