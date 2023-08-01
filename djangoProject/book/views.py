from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from .forms import BookForm

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'book/book_detail.html', {'book': book})


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book/book_form.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'book/book_form.html', {'form': form})