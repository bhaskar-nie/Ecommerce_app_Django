from django.shortcuts import render
from products.models import *
from django.db.models import Q
# Create your views here.
def frontpage(request):
    products=Product.objects.all()[0:8]
    return render(request,'ecom_app/frontpage.html', context={'products':products})

def shop(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    active_category=request.GET.get('category','')

    if active_category:
        products=products.filter(prod_category__slug=active_category)

    query= request.GET.get('query','')

    if query:
        products=products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context={
        'products': products,
        'categories':categories,
        'active_category':active_category,
    }
    return render(request,'ecom_app/shop.html', context)

