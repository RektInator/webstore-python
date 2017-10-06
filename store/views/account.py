from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
import hashlib
import datetime
from django.shortcuts import redirect

def overview(request):
    return renderer.RenderWithContext(request, 'store/account/overview.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST.get("fullname", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        pwhasher = hashlib.sha512()
        pwhasher.update(password.encode('utf-8'))
        hashedpassword = pwhasher.hexdigest()

        try:
            account = models.Accounts.objects.get(fullname=fullname, email=email, password=hashedpassword)

            return renderer.RenderWithContext(request, 'store/account/register.html', 
                {
                    "error": True,
                    "description": "Account already exists."
                }
            )
        except(models.Accounts.DoesNotExist):
            account = models.Accounts(fullname=fullname, email=email, password=hashedpassword, birthday=datetime.datetime.now())
            account.save()
        
            return renderer.RenderWithContext(request, 'store/account/register.html',
                {
                    "error": False,
                    "description": "An activation link has been sent to " + email + ". Please verify your email!",
                    "succeeded": True,
                }
            )
    else:
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

        return redirect("index")
    else:
        return renderer.RenderWithContext(request, 'store/account/login.html')

def logout(request):
    request.session.clear()
    return redirect("index")

def orders(request):
    return renderer.RenderWithContext(request, 'store/account/orders.html', 
        {
            "hasOrders": False
        }
    )