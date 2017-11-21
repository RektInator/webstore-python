from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
from django.shortcuts import redirect

def item(request):

    try:
        requestPath = request.path.split("/")
        action = ""

        if len(requestPath) == 5:
            action = requestPath[4]

        pid = int(requestPath[3])
        product = models.Products.objects.get(id=pid)
        productAdded = False

        if request.method == 'POST':
            if request.session.get("IsLoggedIn", False) == False:
                return redirect("login")

            customer = models.Accounts.objects.get(id=int(request.session.get("UID", 0)))
            if action == "wishlist":
                item = models.Wishlist(customer=customer, product=product)
                item.save()
            elif action == "shoppingcart":
                item = models.Shoppingcart(customer=customer, product=product)
                item.save()

            productAdded = True

        return renderer.RenderWithContext(request, 'store/products/item.html', {
            "product": product,
            "added": productAdded,
            "addedTo": action
        })
    except:
        return renderer.RenderWithContext(request, 'store/products/item.html', {
            "error": True
        })

def queryProducts(request,productcat):
    try:
        products = models.ProductCategories.objects.all()
    
        if productcat != "all":
            products = products.filter(
                category=models.Category.objects.get(url=productcat)
            )

        return renderer.RenderWithContext(request, 'store/products/products.html', {
            "products": products
        })
    except:
        return renderer.RenderWithContext(request, 'store/products/products.html', {
            "error": True
        })

def index(request):
    if len(request.path) <= 10:
        return queryProducts(request, "all")
    else:
        return queryProducts(request, request.path[10:])