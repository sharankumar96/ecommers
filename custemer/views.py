
from django.shortcuts import render

# Create your views here.
def custemer_home(request):
    return render(request,'custemer/home.html')

def mycart(request):
    return render(request,'custemer/cart.html') 

def myorders(request):
    return render(request,'custemer/myorders.html')       

def myprofile(request):
    return render(request,'custemer/myprofile.html')           