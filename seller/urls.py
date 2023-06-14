from django.urls import path
from. import views

app_name = 'seller'

urlpatterns=[
    path('home', views.home, name='s_home'),
    path('add', views.add_product),
    path('view', views.view_product),
]
