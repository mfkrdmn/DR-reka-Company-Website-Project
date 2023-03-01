from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "REKA GLOBAL Admin Page"

admin.site.register(Profile)
admin.site.register(rfq)
admin.site.register(urun)