from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext

def overview(request):
    return render(request, 'store/account/overview.html')

def register(request):
    return render(request, 'store/account/register.html')

def login(request):
    return render(request, 'store/account/login.html')
