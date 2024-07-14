from django.shortcuts import render
from products.models import *
# Create your views here.
def frontpage(request):
    products=Product.objects.all()[0:8]
    return render(request,'ecom_app/frontpage.html', context={'products':products})