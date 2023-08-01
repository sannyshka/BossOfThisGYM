from django.shortcuts import render, redirect
from django.views import View
from .models import Purchase
from .forms import PurchaseForm

class PurchaseListView(View):
    def get(self, request):
        purchases = Purchase.objects.all()
        return render(request, 'purchase/purchase_list.html', {'purchases': purchases})

class PurchaseDetailView(View):
    def get(self, request, pk):
        purchase = Purchase.objects.get(pk=pk)
        return render(request, 'purchase/purchase_detail.html', {'purchase': purchase})

class PurchaseCreateView(View):
    def get(self, request):
        form = PurchaseForm()
        return render(request, 'purchase/purchase_form.html', {'form': form})

    def post(self, request):
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
        return render(request, 'purchase/purchase_form.html', {'form': form})