from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer

def item(request):
    return renderer.RenderWithContext(request, 'store/products/item.html')

def list(request):
    return renderer.RenderWithContext(request, 'store/products/products.html')
