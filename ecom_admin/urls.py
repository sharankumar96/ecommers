from django.urls import path
from . import views

app_name = 'ecom_admin'

urlpatterns = [
  path('home', views.admin_home, name='admin_home'),
]