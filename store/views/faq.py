from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer

def faq(request):
    return renderer.RenderWithContext(request, 'store/faq.html')