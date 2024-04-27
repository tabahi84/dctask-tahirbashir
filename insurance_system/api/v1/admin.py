from django.contrib import admin

from .models import Customer, Quote

class CustomerModelAdmin(admin.ModelAdmin):
    # list_display = [f.name for f in Customer._meta.get_fields()]
    list_display = ['id', 'first_name', 'last_name', 'dob']
admin.site.register(Customer, CustomerModelAdmin)

class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_id', 'policy_type', 'premium', 'coverage', 'state']
admin.site.register(Quote, QuoteModelAdmin)