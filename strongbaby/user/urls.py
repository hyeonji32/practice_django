from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("signup/", views.signup),
    path("", views.find_user),
]