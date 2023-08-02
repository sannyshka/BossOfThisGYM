from rest_framework import viewsets
from .serializers import UserSerializer
from ..models import User
from user.api.pagination import CustomUserPagination
from .filters import UserFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('age')
    serializer_class = UserSerializer
    pagination_class = CustomUserPagination
    filterset_class = UserFilter
