from django.conf.urls import url

from .views import index
from .views import account
from .views import products
from .views import storage
from .views import contact
from .views import faq
from .views import sale

urlpatterns = [
    # account endpoints
    url(r'^account/register', account.register, name='register'),
    url(r'^account/login', account.login, name='login'),
    url(r'^account/logout', account.logout, name='logout'),
    url(r'^account/orders', account.orders, name='orders'),
    url(r'^account/wishlist', account.wishlist, name='wishlist'),
    url(r'^account/', account.overview, name='overview'),
    
    # storage endpoints
    url(r'^storage/image', storage.image, name='image'),

    # products
    url(r'^products/item', products.item, name='item'),
    url(r'^products/', products.index, name='products'),

	# static pages
	url(r'^contact', contact.contact, name='contact'),
	url(r'^faq', faq.faq, name='faq'),
	url(r'^sale', sale.sale, name='sale'),
    url(r'^$', index.main, name='index'),
]
