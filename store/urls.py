from django.conf.urls import url
from django.urls import path

from .views import index
from .views import account
from .views import products
from .views import storage
from .views import contact
from .views import faq
from .views import sale
from .views import terms
from .views import search
from .views import payment
from .views import admin

urlpatterns = [
    # account endpoints
    url(r'^account/register', account.register, name='register'),
    url(r'^account/login', account.login, name='login'),
    url(r'^account/logout', account.logout, name='logout'),
    url(r'^account/orders', account.orders, name='orders'),
    url(r'^account/wishlist', account.wishlist, name='wishlist'),
	url(r'^account/cart', account.cart, name='cart'),
    url(r'^account/', account.overview, name='overview'),
    
    # admin endpoints
    path('admin/user/<int:id>/remove/', admin.remove, name='removeuser'),
    path('admin/user/<int:id>/', admin.user, name='admin'),
    path('admin/', admin.index, name='admin'),

    # storage endpoints
    url(r'^storage/image', storage.image, name='image'),

    # products
    url(r'^products/item', products.item, name='item'),
    url(r'^products/', products.index, name='products'),

	# static pages
	url(r'^contact', contact.contact, name='contact'),
    url(r'^terms', terms.terms, name='terms'),
	url(r'^faq', faq.faq, name='faq'),
	url(r'^sale', sale.sale, name='sale'),
    url(r'^search', search.search, name='search'),
    url(r'^payment', payment.payment, name='payment'),
    url(r'^$', index.main, name='index'),
]
