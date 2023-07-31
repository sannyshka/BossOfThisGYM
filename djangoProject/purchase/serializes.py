from rest_framework import serializers
from .models import Purchase

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('book_id', 'user_id', 'purchase_date')