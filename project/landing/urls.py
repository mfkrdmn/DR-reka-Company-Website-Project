from django.urls import path
from . import views
app_name = "landing"
urlpatterns = [
    path('',views.index, name="index"),
    path('contactus',views.contact, name="contact"),
    path('career',views.career, name="career"),
    path('test',views.test, name="test"),
    path('aviation',views.aviation, name="aviation"),
    path('gse',views.gse, name="gse"),
    path('finance',views.finance, name="finance"),
    path('ec',views.ec, name="ec"),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logout, name="logout"),
    path('rec',views.rec, name="rec"),
    path('profile',views.profile, name="profile"),
    path('milesvolta',views.milesvolta, name="milesvolta"),
    path('comingsoon',views.Soon, name="comingsoon"),
]
