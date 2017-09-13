from django.conf.urls import url

from . import views
from .modules import index

urlpatterns = [
    url(r'^$', index.main, name='index'),
]
