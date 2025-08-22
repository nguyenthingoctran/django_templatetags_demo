from django.urls import path
from screen import views

app_name = 'Screen'

urlpatterns = [
    path("home/", views.Home.as_view(), name="home"),
]