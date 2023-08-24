from django.contrib import admin
from app1.models import *
# Register your models here.

class userdisplay(admin.ModelAdmin):
    list_display=['id','name','email','number','address']
    list_filter=['name','email','number']
    search_fields=['name','number']
admin.site.register(Userregister,userdisplay)


admin.site.register(Category)

class productdisplay(admin.ModelAdmin):
    list_display=['name','price','discription','quantity']
admin.site.register(Product,productdisplay)


class sellerdisplay(admin.ModelAdmin):
    list_display=['id','name','email','number','address']
    list_filter=['name','email','number']
    search_fields=['name','number']
admin.site.register(sellerregister,sellerdisplay)

admin.site.register(Cart)

admin.site.register(Order)