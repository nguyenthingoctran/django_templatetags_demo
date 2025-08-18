from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Research_Doc(TemplateView):
    template_name = "app/research_doc/template_tags_and_filter.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        return data