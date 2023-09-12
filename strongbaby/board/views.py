from django.http import HttpResponse, JsonResponse


def hellos(self):
    print("hello")
    return HttpResponse("Hi")
