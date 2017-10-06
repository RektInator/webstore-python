from django.conf.urls import url

from .views import index
from .views import account
from .views import products
from .views import storage

urlpatterns = [
    # account endpoints
    url(r'^account/register', account.register, name='register'),
    url(r'^account/login', account.login, name='login'),
    url(r'^account/logout', account.logout, name='logout'),
    url(r'^account/orders', account.orders, name='orders'),
    url(r'^account/', account.overview, name='overview'),
    
    # storage endpoints
    url(r'^storage/image', storage.image, name='image'),

    # products
    url(r'^products/item', products.item, name='item'),
    url(r'^products/', products.list, name='products'),

    url(r'^$', index.main, name='index'),
]
