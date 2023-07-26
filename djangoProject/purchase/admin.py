from django.contrib import admin
from .models import Purchase

class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Purchase._meta.fields]

admin.site.register(Purchase, PurchaseModelAdmin)
