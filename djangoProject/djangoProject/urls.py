"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import users_view
from user.views import UserListView, UserDetailView, UserCreateView
from purchase.views import PurchaseListView, PurchaseDetailView, PurchaseCreateView
from book.views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_view),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('purchase/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('purchase/create/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
]
