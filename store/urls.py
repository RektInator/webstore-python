from django.conf.urls import url

from . import views
from .modules import index

urlpatterns = [
    # url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': '/'}),
    url(r'^$', index.main, name='index'),
]
