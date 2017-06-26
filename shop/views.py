from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib import auth

# Create your views here.
from shop.models import Category, SubCategory, Customer


def about(request):
    return render(request, 'about.html', {"title": "About"})

def care(request):
    return render(request, 'care.html', {"title": "Personal Care"})

def codes(request):
    return render(request, 'codes.html', {"title": "Codes"})

def contact(request):
    return render(request, 'contact.html', {"title": "Contact"})

def faqs(request):
    return render(request, 'faqs.html', {"title": "About"})

def hold(request):
    return render(request, 'hold.html', {"title": "House hold"})

def products(request, category, subcategory=None, id=None):
    # print("View products")
    # print("category: " + str(category))
    # print("subcategory: " + str(subcategory))
    # print("id: " + str(id))
    categories = Category.objects.all()

    # if subcategory is None:
    #     # отрендерить страницу для категории
    #     c = get_object_or_404(Category, slug__exact=category)  # Category.objects.get(name__exact=category)
    #     pass
    # if id is None:
    #     # отрендерить страницу для категории
    #     c = get_object_or_404(Category, slug__exact=category)  # Category.objects.get(name__exact=category)
    #     s = get_object_or_404(SubCategory, slug__exact=subcategory)
    #     pass
    # if id:
    #     print(type(id))
    #     # отрендерить страницу для товара
    #     c = get_object_or_404(Category, slug__exact=category)  # Category.objects.get(name__exact=category)
    #     s = get_object_or_404(SubCategory, slug__exact=subcategory)
    #     if s.category != c:
    #         raise Http404
    #     p = s.product_set.get(pk=int(id))
    # s = categories.subcategory_set.get(pk=1)
    # print(s)
    # p = s.product_set.all()
    # print(p)
    return render(request, 'index.html', {"title": "Home page",
                                          'categories': categories,
                                          #'products': p})
                                          })

def index(request):
    # c = Category.objects.get(pk=1)
    # s = c.subcategory_set.get(pk=1)
    # print(s)
    # p = s.product_set.all()
    # print(p)
    return render(request, 'index.html', {'title': 'Home page',
                                          #'categories': Category.objects.all(),
                                          #'products': p,
                                          })

def kitchen(request):
    return render(request, 'kitchen.html', {"title": "Kitchen"})

def login(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = auth.authenticate(username=username, password=password)
    # if user is not None and user.is_active:
    #     # Правильный пароль и пользователь "активен"
    #     auth.login(request, user)
    #     # Перенаправление на "правильную" страницу
    #     return render(request, 'login.html', {'title': 'Login'})
    #     #return HttpResponseRedirect("/account/loggedin/")
    # else:
    #     # Отображение страницы с ошибкой
    #     return render(request, 'login.html', {'title': 'Home page'})
    #     #return HttpResponseRedirect("/account/invalid/")
    return render(request, 'login.html', {"title": "Login"})

def register(request):

    return render(request, 'register.html', {"title": "Register"})

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    pass
    #return HttpResponseRedirect("/account/loggedout/")


def offer(request):
    return render(request, 'offer.html', {"title": "Offer"})


def shipping(request):
    return render(request, 'shipping.html', {"title": "Shipping"})

def single(request):
    return render(request, 'single.html', {"title": "Single"})

def terms(request):
    return render(request, 'terms.html', {"title": "Terms And Conditions"})

def wishlist(request):
    return render(request, 'wishlist.html', {"title": "About"})

