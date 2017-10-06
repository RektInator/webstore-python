from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
import hashlib

def overview(request):
    return renderer.RenderWithContext(request, 'store/account/overview.html')

def register(request):
    return renderer.RenderWithContext(request, 'store/account/register.html')

def login(request):
    if request.method == 'POST':
        
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        pwhasher = hashlib.sha512()
        pwhasher.update(password.encode('utf-8'))
        hashedpassword = pwhasher.hexdigest()

        try:
            account = models.Accounts.objects.get(email=email, password=hashedpassword)

            request.session["Fullname"] = account.fullname
            request.session["Email"] = account.email
            request.session["IsLoggedIn"] = True
            request.session["UID"] = 0

        except (models.Accounts.DoesNotExist):
            return renderer.RenderWithContext(request, 'store/account/login.html',
                {
                    "error": True,
                    "description": "Account not found.",
                }
            )

        return HttpResponse(hashedpassword)

    else:
        return renderer.RenderWithContext(request, 'store/account/login.html')