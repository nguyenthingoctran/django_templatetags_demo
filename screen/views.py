from django.views.generic.base import TemplateView

class Home(TemplateView):
  template_name = "app/screen/home.html"

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['person'] = 'John'
    data['greeting'] = 'Hello'
    return data