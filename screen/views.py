from django.views.generic.base import TemplateView

class Home(TemplateView):
  template_name = "app/screen/home.html"

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    return data

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")