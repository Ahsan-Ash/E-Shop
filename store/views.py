from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.

def index(request):
    products = Product.get_all_products()
    print(products)
    # return HttpResponse('<h1>Index Page</h1>')
    return render(request, 'store/index.html', {'products' : products})