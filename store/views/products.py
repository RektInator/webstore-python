from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
from django.shortcuts import redirect

def item(request):

    #try:
        requestPath = request.path.split("/")
        action = ""

        if len(requestPath) == 5:
            action = requestPath[4]

        pid = int(requestPath[3])
        product = models.Products.objects.get(id=pid)
        productAdded = False
        error = False
        errorMessage = ""
        productRemoved = False
        edit = False
        image = models.Image.objects.all()

        if request.method == 'POST':

            productSize = request.POST.get("size", "")

            if request.session.get("IsLoggedIn", False) == False:
                return redirect("login")

            customer = models.Accounts.objects.get(id=int(request.session.get("UID", 0)))
            if action == "wishlist":
                existingEntry = models.Wishlist.objects.filter(customer=customer, product=product)

                if existingEntry.exists():
                    existingEntry.delete()
                    productRemoved = True
                else:
                    item = models.Wishlist(customer=customer, product=product)
                    item.save()

                productAdded = True
            elif action == "shoppingcart":
                if productSize != "":
                    item = models.Shoppingcart(customer=customer, product=product, type=models.ProductSize.objects.get(id=int(productSize)))
                    item.save()
                    productAdded = True
                else:
                    error = True
                    productAdded = False
                    errorMessage = "You must choose a product size."
            elif action == "edit":
                edit = False
                if len(request.POST.get("name", "")) > 0:
                    product.name = request.POST.get("name", product.name)
                if len(request.POST.get("desc", "")) > 0:
                    product.description = request.POST.get("desc", product.description)
                
                product.image.url = request.FILES['myfile'].name

                product.image.save()
                product.save()
              
        else:
            if action == "edit":
                edit = True
                
        return renderer.RenderWithContext(request, 'store/products/item.html', {
            "product": product,
            "image": image,
            "added": productAdded,
            "addedTo": action,
            "size": models.ProductSize.objects.all(),
            "error": error,
            "errorMessage": errorMessage,
            "productFound": True,
            "removed": productRemoved,
            "edit": edit,
        })
    #except:
     #   return renderer.RenderWithContext(request, 'store/products/item.html', {
      #      "productFound": False
       # })

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