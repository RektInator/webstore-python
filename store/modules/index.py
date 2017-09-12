from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext

def main(request):
    return render(RequestContext(request), 'store/index.html')

