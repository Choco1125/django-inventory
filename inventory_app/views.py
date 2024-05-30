from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world!</h1>')

def hello(request, name):
    return HttpResponse('<h1>Hello %s</h1>' % name)

def products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)
