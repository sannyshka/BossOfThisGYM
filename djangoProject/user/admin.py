from django.contrib import admin
from .models import User

class UserModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

admin.site.register(User, UserModelAdmin)