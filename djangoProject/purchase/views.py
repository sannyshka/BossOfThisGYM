from django.shortcuts import render
from django.http import JsonResponse
from .models import Purchase

def purchase_list(request):
    purchases = Purchase.objects.all()
    data = [{'user': purchase.user.name, 'book': purchase.book.title, 'purchase_date': purchase.purchase_date} for purchase in purchases]
    return JsonResponse(data, safe=False)
