from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
from django.shortcuts import redirect
import datetime

def payment(request):
  if request.method == 'POST':
    customer = models.Accounts.objects.get(id=int(request.session.get("UID", 0)))
    cart = models.Shoppingcart.objects.all().filter(customer=customer, order=None)

    if cart.count() == 0:
      return redirect("index")

    totalprice = 0
    for item in cart:
      totalprice += float(item.type.price)

    order = models.Orders(customer=customer, date=datetime.datetime.now(), price=totalprice)
    order.save()

    for item in cart:
      item.order = order
      item.save()

    return renderer.RenderWithContext(request, 'store/account/overview.html')
  else:
    customer = models.Accounts.objects.get(id=int(request.session.get("UID", 0)))

    return renderer.RenderWithContext(request, 'store/payment.html',
    {
      "customer": customer
    })