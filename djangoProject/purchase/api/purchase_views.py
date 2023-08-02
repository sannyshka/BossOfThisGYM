from rest_framework import viewsets
from .serializers import PurchaseSerializer
from ..models import Purchase
from .filters import PurchaseFilter

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('purchase_date')
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter