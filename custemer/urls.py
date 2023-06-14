from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
   path('home', views.custemer_home, name='c_home'),
   path('orders', views.myorders),
   path('cart', views.mycart),
   path('profile', views.myprofile),

]