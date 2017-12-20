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

        if request.method == 'POST':
            fullname = request.POST.get("name", "")
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            administrator = request.POST.get("admin", "off")

            if len(fullname) > 0:
                user.fullname = fullname
            if len(email) > 0:
                user.email = email
            if len(password) > 0:
                # todo!
                pass
            if administrator == "on":
                user.administrator = 1
            else:
                user.administrator = 0
            
            user.save()

        return renderer.RenderWithContext(request, 'store/admin/user.html', {
            "user": user
        })
    except:
        return redirect("admin")

def index(request):
    return renderer.RenderWithContext(request, 'store/admin/overview.html', {
        "users": models.Accounts.objects.all()
    })