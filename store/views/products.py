from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext

def item(request):
    return render(request, 'store/products/item.html')

def list(request):
    return render(request, 'store/products/products.html')
