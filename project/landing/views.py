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