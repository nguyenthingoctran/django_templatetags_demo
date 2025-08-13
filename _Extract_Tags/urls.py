from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index),
    path("table_demo/", views.table_demo),
]