from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")


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