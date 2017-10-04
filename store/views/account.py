from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer

def overview(request):
    return renderer.RenderWithContext(request, 'store/account/overview.html')

def register(request):
    return renderer.RenderWithContext(request, 'store/account/register.html')

def login(request):
    if request.method == 'POST':
        
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        return HttpResponse(username)
    else:
        return renderer.RenderWithContext(request, 'store/account/login.html')