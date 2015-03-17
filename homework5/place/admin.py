from django.contrib import admin
from place.models import Country,City
# Register your models here.

admin.site.register(Country, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)