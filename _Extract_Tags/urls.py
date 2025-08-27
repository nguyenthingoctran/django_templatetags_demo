from django.urls import path
from _Extract_Tags import views

app_name = '_Extract_Tag'

urlpatterns = [
    path("table_demo/", views.DataTable.as_view(), name='table_advanced_demo'),
    path("guide/", views.ListGuide.as_view(), name='list_guide'),
    path("title/", views.Title.as_view(), name='title'),
    path("breadcrumbs/", views.Breadcrumbs.as_view(), name='breadcrumbs'),
    path("modals/", views.Modals.as_view(), name='modals'),
    path("alert/", views.Alert.as_view(), name='alert'),
]