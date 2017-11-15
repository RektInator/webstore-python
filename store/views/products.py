from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models

def item(request):
    return renderer.RenderWithContext(request, 'store/products/item.html')

def queryProducts(request,productcat):
    products = models.ProductCategories.objects.all()
    
    if productcat != "all":
        products = products.filter(
            category=models.Category.objects.get(url=productcat)
        )

    return renderer.RenderWithContext(request, 'store/products/products.html', {
        "products": products
    })

def index(request):
    if len(request.path) <= 10:
        return queryProducts(request, "all")
    else:
        return queryProducts(request, request.path[10:])