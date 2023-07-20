from django.db import models
from user.models import User
from book.models import Book
from django.contrib.auth.models import User

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-purchase_date']

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'