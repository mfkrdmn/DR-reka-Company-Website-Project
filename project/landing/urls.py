from django.urls import path
from . import views
app_name = "landing"

#forgot password
from django.contrib.auth import views as auth_views
#

urlpatterns = [
    path('',views.yonlendirme, name="yonlendirme"),
    path('home',views.index, name="index"),
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
    path('<int:id>/<str:slug>/',views.milesvolta, name="milesvolta"),
    #product
    path('product',views.product_list, name="product_list"),
    #product
    path('companyprofile',views.companyprofile, name="companyprofile"),
    #passwordforgot
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),

]
