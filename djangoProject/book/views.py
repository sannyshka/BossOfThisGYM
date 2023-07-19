from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    data = [{'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return JsonResponse(data, safe=False)
