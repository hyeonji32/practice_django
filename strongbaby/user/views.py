from django.http import HttpResponse, JsonResponse
import json
from .models import User


def hello(self):
    print("aaa")
    print(self)
    return HttpResponse("안녕하세요")


def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        password = data['password']
        user = User(name, password)
        user.save()
    return HttpResponse("ok")


def find_user(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        id = data['id']
        user = User.objects.get(id=id)
        context = {
            "user_id": user.id,
            "name": user.name,
            "password": user.password
        }
    return JsonResponse(context)


def update_user(request, user_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        user = User.objects.get(id=user_id)
        user.id = user_id
        user.name = data["name"]
        user.password = data["password"]
        user.save()
        context = {
            "id": user.id,
            "name": user.name,
            "password": user.password
        }
    return JsonResponse(context)

