from django.urls import path
from _Extract_Tags.views import DataTable

from . import views

urlpatterns = [
    path("index/", views.index),
    path("table_demo/", DataTable.as_view()),
]