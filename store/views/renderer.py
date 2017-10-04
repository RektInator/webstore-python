from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext

def RenderWithContext(request, page):
    context = {}

    context["IsLoggedIn"] = request.session.get("IsLoggedIn", False)
    context["Fullname"] = request.session.get("Fullname", "")
    context["Email"] = request.session.get("Email", "")
    context["UID"] = request.session.get("UID", 0)

    return render(request, page, context)