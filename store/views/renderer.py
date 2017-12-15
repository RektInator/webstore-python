from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from . import models

def RenderWithContext(request, page, context = {}):
    context["IsLoggedIn"] = request.session.get("IsLoggedIn", False)
    context["Fullname"] = request.session.get("Fullname", "")
    context["Email"] = request.session.get("Email", "")
    context["UID"] = request.session.get("UID", 0)
    context["IsAdmin"] = request.session.get("IsAdmin", False)
    context["categories"] = models.Category.objects.all()

    if context["IsLoggedIn"]:
        customer = models.Accounts.objects.get(id=int(request.session.get("UID", 0)))
        cart = models.Shoppingcart.objects.all().filter(customer=customer, order=None)
        context["ShoppingCartItems"] = cart.count()

    return render(request, page, context)