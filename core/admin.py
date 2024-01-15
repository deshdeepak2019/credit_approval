

# Register your models here.

from django.contrib import admin

# Register your models here.

from .models import Customer

@admin.register(Customer)
class Customer(admin.ModelAdmin):
    model=Customer
    # list_display=