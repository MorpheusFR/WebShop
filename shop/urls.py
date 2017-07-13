from django.conf.urls import url

from .views import \
    index, \
    contact, \
    about, \
    login, \
    care, \
    codes, \
    faqs, \
    hold, \
    kitchen, \
    offer, \
    register, \
    shipping, \
    single, \
    terms, \
    wishlist, products

urlpatterns = [
    # url(r'^$', index),
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', login, name='logout'),
    url(r'^register/$', register, name='register'),

    url(r'^contact/$', contact, name='contact'),
    url(r'^care/$', care, name='care'),
    url(r'^codes/$', codes, name='codes'),
    url(r'^faqs/$', faqs, name='faqs'),
    url(r'^hold/$', hold, name='hold'),

    url(r'^offer/$', offer, name='offer'),

    url(r'^shipping/$', shipping, name='shipping'),
    url(r'^single/$', single, name='single'),
    url(r'^terms/$', terms, name='terms'),
    url(r'^wishlist/$', wishlist, name='wishlist'),
    url(r'^about/$', about, name='about'),
    url(r'^(?P<slug_category>\w+)/(?P<slug_subcategory>\w*)/?(?P<id>\d*)$', products, name='products'),

    url(r'^kitchen/$', kitchen, name='kitchen'),
]
