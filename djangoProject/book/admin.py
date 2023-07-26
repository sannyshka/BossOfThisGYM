from django.contrib import admin
from .models import Book

class BookModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]

admin.site.register(Book, BookModelAdmin)