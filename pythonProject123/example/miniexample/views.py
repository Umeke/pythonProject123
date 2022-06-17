from django.shortcuts import render

from django.http import HttpResponse

from .models import Product

def index(request):
    product = Product
    return HttpResponse(product[0].object.all())

