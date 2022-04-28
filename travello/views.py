from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination, Item, ToDoList, ContactDetails, NewsTeller

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contactUs(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')

def database(request, id):
    lis = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % lis.name)

def insertContactDetails(request):
    name = request.GET['name']
    email = request.GET['email']
    phoneNo = request.GET['phone']
    message = request.GET['message']
    details = ContactDetails(name=name, email=email, phone=phoneNo, message=message)
    details.save()
    return render(request, 'index.html')

def newsTellerSub(request):
    email = request.GET['email']
    newsteller = NewsTeller(email=email)
    newsteller.save()
    return render(request, 'index.html')

def service(request):
    dest1 = Destination()
    dest1.name = 'Bali'
    dest1.price = 69000
    dest1.img = 'img'
    dest1.desc = 'This is a wonderful place'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Maldives'
    dest2.price = 80000
    dest2.img = 'img'
    dest2.desc = 'This is also wonderful place'
    dest1.offer = False

    dest3 = Destination()
    dest3.name = 'Bali'
    dest3.price = 89000
    dest3.img = 'img'
    dest3.desc = 'This is beautiful place'
    dest1.offer = True

    dests = [dest1, dest2, dest3]
    return render(request, 'service.html', {'dests': dests})
