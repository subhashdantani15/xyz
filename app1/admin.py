from django.contrib import admin
from app1.models import *
# Register your models here.


class userdisplay(admin.ModelAdmin):
    list_display=['name','email','number','address']
    list_filter=['name','email','number','address']
    search_fields=['name','number']
admin.site.register(Userregister,userdisplay)

admin.site.register(Category)

class productdisplay(admin.ModelAdmin):
    list_display=['name','price','quantity']

admin.site.register(Product,productdisplay)

admin.site.register(Contactus)


class vendoordisplay(admin.ModelAdmin):
    list_display=['name','email','number','address']
    list_filter=['name','email','number','address']
    search_fields=['name','number']
admin.site.register(Vendorregister,vendoordisplay)

admin.site.register(Cart)
class orderdisplay(admin.ModelAdmin):
    list_display=['name','email','number','address',"totalprice",'datetime']
admin.site.register(Order,orderdisplay)

admin.site.site_header="E-shop administration"
admin.site.site_title="E-shop"
admin.site.index_title="E-shop"