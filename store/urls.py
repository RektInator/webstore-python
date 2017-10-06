from django.conf.urls import url

from .views import index
from .views import account
from .views import products

urlpatterns = [
    url(r'^account/register', account.register, name='register'),
    url(r'^account/login', account.login, name='login'),
    url(r'^account/logout', account.logout, name='logout'),
    url(r'^account/', account.overview, name='overview'),
    
    url(r'^products/item', products.item, name='item'),
    url(r'^products/', products.list, name='products'),

    url(r'^$', index.main, name='index'),
]
