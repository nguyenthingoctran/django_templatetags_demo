from django.urls import path
from research_doc import views

app_name = 'Research_Doc'

urlpatterns = [
    path("django_templatetags/", views.Django_Templatetags.as_view(), name='django_templatetags'),
    path("javascript/", views.Javascript.as_view(), name='javascript'),
    path("scss/", views.Scss.as_view(), name='scss'),
]