from django.urls import path
from . import views

urlpatterns = [
    path("", views.message_list, name="message_list"),
    path("sobre/", views.about, name="about"),
    path("novo/", views.message_create, name="message_create")
]

