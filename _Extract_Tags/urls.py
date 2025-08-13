from django.urls import path

from . import views

urlpatterns = [
    path("table_demo/", views.index),
]