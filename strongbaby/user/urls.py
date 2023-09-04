from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("signup/", views.signup),
    path("", views.find_user),
    path("update/<int:user_id>/", views.update_user)
]
