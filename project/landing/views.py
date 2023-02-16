from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
# Create your views here.
# Create your views here.

def index(request):

    if request.method == "POST":
        PartNumber = request.POST['PartNumber']
        Description = request.POST['Description']
        Quantity = request.POST['Quantity']
        Condition = request.POST['Condition']
        Mail = request.POST['Mail']
        Telephone = request.POST['Telephone']
        CompanyName = request.POST['CompanyName']
        fullname = request.POST['fullname']

        if request.method == "POST":

            newRFQ = rfq.objects.create(PartNumber=PartNumber, Description=Description, 
            Quantity=Quantity,Condition=Condition,Mail=Mail,Telephone=Telephone,CompanyName=CompanyName,fullname=fullname)
            newRFQ.save()
            return redirect('/')
    
    
    return render(request, 'index.html')

#############

def contact(request):
    return render(request,"contact.html")

def career(request):
    return render(request,"career.html")

def test(request):
    return render(request,"test.html")

def aviation(request):
    return render(request,"aviation.html")
    
def gse(request):
    return render(request,"gse.html")

def finance(request):
    return render(request,"finance.html")

def ec(request):
    return render(request,"ec.html")

def rec(request):
    return render(request,"rec.html")


#############


@login_required(login_url='/login')
def profile(request):
        return render(request,"profile.html")

#############

def login(request):
    if request.method == 'POST':
        companyName = request.POST['companyName']
        password = request.POST['password']

        user = auth.authenticate(username=companyName, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User is Invalid!')
            return redirect('/login')
    else:
        return render(request, 'login.html')

#############

def register(request):
    
    if request.method == "POST":
        email = request.POST['email']
        companyName = request.POST['companyName']
        password = request.POST['password']
        password_again = request.POST['password_again']

        if password == password_again:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken :(")
                return redirect("register")
            elif User.objects.filter(username=companyName).exists():
                messages.info(request, "Username is already taken :(")
                return redirect("register")
            else:
                user = User.objects.create_user(username=companyName, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=companyName, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=companyName)
                new_profile = Profile.objects.create(user=user_model, email=email,companyName=companyName )
                new_profile.save()
                return redirect('/login')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


#############


def logout(request):
    auth.logout(request)
    messages.error(request, "You are logged out")
    return redirect("login")


############ GSE Individuals ##############

def milesvolta(request):
    return render(request,"milesvolta.html")