from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={                                                  
        "variable1":"Dipak is great",
        "variable2":"Dipak is backend developer",
        "variable3":"Dipak is multitasker"
    
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Services page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")

    return render(request, 'contact.html')
    #return HttpResponse("This is Contact page")

def Spofty(request):
    return render(request, 'spofty.html')
    #return HttpResponse("This is amazing page")

def Ice_Cream(request):
    return render(request, 'ice_cream.html')
    #return HttpResponse("This is unique page")

def Family_Pack(request):
    return render(request, 'family_pack.html')
    #return HttpResponse("This is icecream price page")

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("This is Ice Cream home page")

