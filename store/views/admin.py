from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
import hashlib
import datetime
from django.shortcuts import redirect

def index(request):
    return renderer.RenderWithContext(request, 'store/admin/overview.html')