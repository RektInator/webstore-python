from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models

def item(request):

    try:
        product = models.Products.objects.get(id=int(request.path[15:]))

        return renderer.RenderWithContext(request, 'store/products/item.html', {
            "product": product
        })
    except:
        return renderer.RenderWithContext(request, 'store/products/item.html', {
            "error": True
        })

def queryProducts(request,productcat):
    try:
        products = models.ProductCategories.objects.all()
    
        if productcat != "all":
            products = products.filter(
                category=models.Category.objects.get(url=productcat)
            )

        return renderer.RenderWithContext(request, 'store/products/products.html', {
            "products": products
        })
    except:
        return renderer.RenderWithContext(request, 'store/products/products.html', {
            "error": True
        })

def index(request):
    if len(request.path) <= 10:
        return queryProducts(request, "all")
    else:
        return queryProducts(request, request.path[10:])