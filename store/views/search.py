from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from . import renderer
from . import models
from django.shortcuts import redirect

def search(request):
    try:
        products = models.Products.objects.all()
        matchFound = False

        if request.method == 'POST':
            search_input = request.POST.get("search_term", None);

            foundproduct = []
            for p in products:
                if (search_input in p.name.lower()) | (search_input in p.name.upper()) :
                    matchFound = True
                    foundproduct.append(p)
            
            
        return renderer.RenderWithContext(request, 'store/search.html', {
            "search_input": search_input,
            "foundproduct": foundproduct,
            "matchFound": matchFound
        })

    except:
        return renderer.RenderWithContext(request, 'store/search.html', {
            "matchFound": False
        })