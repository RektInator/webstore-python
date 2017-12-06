from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
from django.shortcuts import redirect

def payment(request):

  customer = models.Accounts.objects.get(id=int(request.session.get("UID", 0)))
  
  return renderer.RenderWithContext(request, 'store/payment.html',
  {
    "customer": customer
  })