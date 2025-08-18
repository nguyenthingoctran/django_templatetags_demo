from django.urls import path
from _Extract_Tags import views

app_name = '_Extract_Tag'

urlpatterns = [
    path("index/", views.index),
    path("table_demo/", views.DataTable.as_view(), name='table_advanced_demo'),
]