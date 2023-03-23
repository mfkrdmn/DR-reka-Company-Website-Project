from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
# Create your views here.
# Create your views here.
from django.shortcuts import render

from django.shortcuts import render
from django.utils.translation  import gettext as _
from django.utils.translation import get_language, activate, gettext
def dil_bilgisi():
    return get_language()
#translate
def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('Hello')
        
    finally:
        activate(cur_language)
    return text
#translate
from django.core.mail import EmailMessage

def send_email(request,PartNumber,Description,Quantity,Condition,Mail,Telephone,CompanyName,fullname):
    govde= """PartNumber = {}
Description = {}
Quantity = {}
Condition = {}
Mail = {}
Telephone = {}
Company Name = {}
full name= {}
    """.format(PartNumber,Description,Quantity,Condition,Mail,Telephone,CompanyName,fullname)
    email = EmailMessage(
        'Sipariş',
        govde,
        'rekaglobal1@gmail.com',
        ['mfkrdmn@gmail.com'],
        reply_to=['rekaglobal1@gmail.com'],
        headers={'Message-ID': 'foo'},
    )
    email.send()
def index(request):
    dil = dil_bilgisi()
    trans = translate(language='English')
    link = ""
    if request.method == "POST":
        PartNumber = request.POST['PartNumber']
        Description = request.POST['Description']
        Quantity = request.POST['Quantity']
        Condition = request.POST['Condition']
        Mail = request.POST['Mail']
        Telephone = request.POST['Telephone']
        CompanyName = request.POST['CompanyName']
        fullname = request.POST['fullname']
        send_email(request,PartNumber,Description,Quantity,Condition,Mail,Telephone,CompanyName,fullname)
        if request.method == "POST":

            newRFQ = rfq.objects.create(PartNumber=PartNumber, Description=Description, 
            Quantity=Quantity,Condition=Condition,Mail=Mail,Telephone=Telephone,CompanyName=CompanyName,fullname=fullname)
            newRFQ.save()
            return redirect('/')
    
    
    return render(request, 'index.html',{"trans":trans,"dil":dil,"link":link})

#############

def contact(request):
    dil = dil_bilgisi()
    trans = translate(language='English')
    link = "contactus"
    return render(request,"contact.html",{"trans":trans,"dil":dil,"link":link})

def career(request):
    dil = dil_bilgisi()
    trans = translate(language='English')
    link = "career"
    return render(request,"career.html",{"trans":trans,"dil":dil,"link":link})

def test(request):
    dil = dil_bilgisi()
    trans = translate(language='English')
    return render(request,"test.html",{"trans":trans,"dil":dil})

def aviation(request):
    dil = dil_bilgisi()
    link = "aviation"
    trans = translate(language='English')
    return render(request,"aviation.html",{"trans":trans,"dil":dil,"link":link})
    
def gse(request):
    trans = translate(language='English')
    ur = urun.objects.all()
    link = "gse"
    dil = dil_bilgisi()
    return render(request,"gse.html",{"trans":trans,"dil":dil,"ur":ur,"link":link})

def finance(request):
    dil = dil_bilgisi()
    link = "finance"
    trans = translate(language='English')
    return render(request,"finance.html",{"trans":trans,"dil":dil,"link":link})

def ec(request):
    dil = dil_bilgisi()
    link = "ec"
    trans = translate(language='English')
    return render(request,"ec.html",{"trans":trans,"dil":dil,"link":link})

def rec(request):
    trans = translate(language='English')
    link = "rec"
    dil = dil_bilgisi()
    return render(request,"rec.html",{"trans":trans,"dil":dil,"link":link})


from .forms import * 
def companyprofile(request):
    trans = translate(language='English')
    dil = dil_bilgisi()
    link = "companyprofile"
    content = {"trans":trans,"dil":dil, "link":link}
    prr = get_object_or_404(Profile,user_id = request.user.id)
    if dil_bilgisi() == "Turkish":
        form = profile_edit_tr(request.POST or None,request.FILES or None,instance = prr)
    elif dil_bilgisi() == "English":
        form = profile_edit_en(request.POST or None,request.FILES or None,instance = prr)
    elif dil_bilgisi() == "Arabic":
        form = profile_edit_ar(request.POST or None,request.FILES or None,instance = prr)
    else:
        form = profile_edit_de(request.POST or None,request.FILES or None,instance = prr)
    content['form']=  form
    content["profile"] = prr
    if form.is_valid():
        profile = form.save(commit=False)
        profile.save()
        y = "/"+dil_bilgisi()+"/companyprofile"
        return redirect(y)
    return render(request,"companyprofile.html",content)


#############


@login_required(login_url='/login')
def profile(request):
        dil = dil_bilgisi()
        trans = translate(language='en')
        dil = dil_bilgisi()
        link = "profile"
        content = {"trans":trans,"dil":dil, "link":link}
        return render(request,"profile.html",content)

#############

def login(request):
    dil = dil_bilgisi()
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
    dil = dil_bilgisi()
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
    return redirect('/')


############ GSE Individuals ##############
from .models import urun
from django.shortcuts import render,get_object_or_404
def milesvolta(request,id,slug):
    urunler = get_object_or_404(urun, id = id)
    dil = dil_bilgisi()
    content ={}
    content["dil"] = dil
    content["urun"] = urunler
    return render(request,"milesvolta.html",content)

def product_list(request):
    dil = dil_bilgisi()
    content ={}
    content["dil"] = dil
    products = all_product.objects.filter(qty__gt=0)
    
    #__contains =
    if request.GET:
        key = request.GET.get("key")
        if key:
            products = all_product.objects.filter(qty__gt=0,ac_type__contains = key)
    content["product"] = products
    return render(request,"product.html",content)