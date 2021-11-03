from django.contrib import admin

from cakeshop.models import Cake, Flavor

# Register your models here.

admin.site.register(Cake)
admin.site.register(Flavor)
