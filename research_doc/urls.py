from django.urls import path
from research_doc import views

app_name = 'Research_Doc'

urlpatterns = [
    path("index/", views.Research_Doc.as_view(), name='research_doc_index'),
]