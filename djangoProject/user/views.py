from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import UserForm


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/user_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'user/user_detail.html', {'user': user})

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user/user_form.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user/user_form.html', {'form': form})