from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import User


# Create your views here.


def hello(self):
    print("aaa")
    print(self)
    return HttpResponse("안녕하세요")


def signup(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        user_id = data['user_id']
        password = data['password']
        user = User(user_id, password)
        user.save()
    return HttpResponse("ok")
