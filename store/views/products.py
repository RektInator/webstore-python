from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models

def item(request):
    return renderer.RenderWithContext(request, 'store/products/item.html')

def queryProducts(request,productcat):
    products = models.ProductCategories.objects.all().filter(
        category=models.Category.objects.get(name=productcat)
    )

    return renderer.RenderWithContext(request, 'store/products/products.html', {
        "products": products
    })

def cards(request):
    return queryProducts(request, "card")

def posters(request):
    return queryProducts(request, "poster")

def canvas(request):
    return queryProducts(request, "canvas")

