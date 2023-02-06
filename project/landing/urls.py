from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('contactus',views.contact, name="contact"),
    path('career',views.career, name="career"),
    path('test',views.test, name="test"),
]
