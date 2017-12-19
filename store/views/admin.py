from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
import hashlib
import datetime
from django.shortcuts import redirect

def remove(request, id):
    try:
        user = models.Accounts.objects.get(id=id)
        user.delete()
        
        return redirect("admin")
    except:
        return redirect("admin")

def user(request, id):
    try:
        user = models.Accounts.objects.get(id=id)
        return renderer.RenderWithContext(request, 'store/admin/user.html', {
            "user": user
        })
    except:
        return redirect("admin")

def index(request):
    return renderer.RenderWithContext(request, 'store/admin/overview.html', {
        "users": models.Accounts.objects.all()
    })