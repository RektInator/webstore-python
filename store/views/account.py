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
        # account details
        fullname = request.POST.get("fullname", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # shipping information
        

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
            if '@' not in email:
                return renderer.RenderWithContext(request, 'store/account/register.html',
                {
                    "error": True,
                    "description": "Please enter valid email",
                }
            )
            else:
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
            request.session["UID"] = account.id

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
	if request.session.get("IsLoggedIn", False):
		return renderer.RenderWithContext(request, 'store/account/orders.html', 
			{
				"hasOrders": False
			}
		)
	else:
		return redirect("login")

def wishlist(request):
    if request.session.get("IsLoggedIn", False):
        try:
            customer = models.Accounts.objects.get(id=request.session.get("UID", 0))
            products = models.Wishlist.objects.get(customer=customer)
            return renderer.RenderWithContext(request, 'store/account/wishlist.html', 
                {
				    "hasProducts": True,
                    "products": products
                }
            )
        except:
            return renderer.RenderWithContext(request, 'store/account/wishlist.html', 
                {
                    "hasProducts": False
                }
            )
    else:
        return redirect("login")

def cart(request):
	if request.session.get("IsLoggedIn", False):
		return renderer.RenderWithContext(request, 'store/account/cart.html', 
			{
				"hasProducts": False
			}
		)
	else:
		return redirect("login")