from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    # products_list = Products
    products = Products.objects.all()
    return render(request, 'index.html',{'products': products})


