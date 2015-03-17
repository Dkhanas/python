from django.contrib import admin
from shops.models import TypeShop, Shop

admin.site.register(TypeShop, admin.ModelAdmin)
admin.site.register(Shop, admin.ModelAdmin)
