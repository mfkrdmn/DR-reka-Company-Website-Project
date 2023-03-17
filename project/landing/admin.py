from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "REKA GLOBAL Admin Page"

admin.site.register(Profile)
admin.site.register(rfq)
admin.site.register(urun)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pn', 'size', 'condition','ac_type','qty')
admin.site.register(all_product, BookAdmin)
