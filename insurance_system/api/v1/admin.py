from django.contrib import admin

from .models import Customer

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Customer._meta.get_fields()]
admin.site.register(Customer, CustomerModelAdmin)