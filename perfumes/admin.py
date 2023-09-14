from django.contrib import admin
from perfumes.models import *
# Register your models here.


@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    pass


@admin.register(brand)
class brandadmin(admin.ModelAdmin):
    pass

@admin.register(products)
class productadmin(admin.ModelAdmin):
    pass
@admin.register(productsize)
class productsizeadmin(admin.ModelAdmin):
    pass

@admin.register(feedback)
class feedbackadmin(admin.ModelAdmin):
    list_display=('name','phone','email','message')


@admin.register(review)
class reviewadmin(admin.ModelAdmin):
    list_display=( 'productsid', 'username','rating','message','photo')    