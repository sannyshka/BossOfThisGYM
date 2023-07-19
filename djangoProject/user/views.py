from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    data = [{'name': user.name, 'email': user.email, 'age': user.age} for user in users]
    return JsonResponse(data, safe=False)


