from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer

class Product:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description

    def name(self):
        return self.name

    def image(self):
        return self.image

    def description(self):
        return self.description

def item(request):
    return renderer.RenderWithContext(request, 'store/products/item.html')

def cards(request):

    products = [
        Product("Test", "", "")
    ]

    return renderer.RenderWithContext(request, 'store/products/products.html', {
        "products": products
    })

def posters(request):
    return renderer.RenderWithContext(request, 'store/products/products.html')

def canvas(request):
    return renderer.RenderWithContext(request, 'store/products/products.html')
