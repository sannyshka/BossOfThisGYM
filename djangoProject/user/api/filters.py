import django_filters
from user.models import User

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'name': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'age': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }
