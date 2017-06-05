from django.shortcuts import render

# Create your views here.

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
    return render(request, 'hold.html', {"title": "Household"})

def temp_product():
    product = {
        'moong': ['Moong(1 kg)', 'of.png', 'There are many variations of passages of Lorem Ipsum.', '<del>$2.00</del>$1.50'],
        'moong1': ['Moong(1 kg)', 'of.png', 'There are many variations of passages of Lorem Ipsum.', '<del>$2.00</del>$1.50'],


    }
    return product

#conn = sqlite3.connect("posts.sqlite3")
    #cur = conn.cursor()
    #cur.execute("select * from posts")
    #data = cur.fetchall()
    #conn.close()
    #return data

def index(request):
    return render(request, 'index.html', {"title": "Home page", 'product':temp_product()})

def kitchen(request):
    return render(request, 'kitchen.html', {"title": "Kitchen"})

def login(request):
    return render(request, 'login.html', {"title": "Login"})

def offer(request):
    return render(request, 'offer.html', {"title": "Offer"})

def register(request):
    return render(request, 'register.html', {"title": "Register"})

def shipping(request):
    return render(request, 'shipping.html', {"title": "Shipping"})

def single(request):
    return render(request, 'single.html', {"title": "Single"})

def terms(request):
    return render(request, 'terms.html', {"title": "Terms And Conditions"})

def wishlist(request):
    return render(request, 'wishlist.html', {"title": "About"})

