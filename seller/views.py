from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'seller/home.html')

def add_product(request):
    return render(request,'seller/addproduct.html')  

def view_product(request):
    return render(request,'seller/viewproduct.html')   