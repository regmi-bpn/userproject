from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import Contact
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect ("/login")
    return render (request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ("/")
            # A backend authenticated the credentials
        else:
            return render (request, "login.html")
            # No backend authenticated the credentials
    return render (request, 'login.html') 

def logoutUser(request):
    logout(request)
    # Redirect to a success page.    
    return redirect ('/login') 

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact =Contact(email= email, name= name,  phone=phone, description=description, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')


