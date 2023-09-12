from django.urls import path
from . import views

urlpatterns = {
    path("hellos/", views.hellos),
}
