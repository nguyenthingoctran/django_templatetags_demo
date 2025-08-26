from django.views.generic.base import TemplateView
from datetime import datetime

# Create your views here.
class Research_Doc(TemplateView):
    template_name = "app/research_doc/template_tags_and_filter.html"

    def research_doc_autoescape(self):
      data = 'Hello &lt;i&gt;my&lt;/i&gt; World!'
      return data
    
    def research_doc_cycle(self):
      data = ['Apple', 'Banana', 'Cherry', 'Orange', 'Durian']
      return data
    
    def research_doc_cycle_color(self):
      data = 'springgreen'
      return data
    
    def research_doc_filter_add(self):
      context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
        'vegetables': ['Asparagus', 'Broccoli', 'Carrot'],
      }
      return context
    
    def research_doc_filter_date(self):
      data = datetime.now()
      return data
    
    def dict_color(self):
      colors = ['Red', 'Green', 'Blue', '', 'Yellow']
      return colors
    
    def dict_none_color(self):
      colors = ['Red', None, 'Blue', '', 'Yellow']
      return colors

    def dict_sort(self):
      dict_cars = {
        'cars': [
          {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
          {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
          {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
          {'brand': 'Ford', 'model': 'Focus', 'year': 2004}
        ]
      }
      return dict_cars
    
    def escapejs(self):
      data = {
        'var1': 'John\nDoe'
      }
      return data
    
    def filesizeformat(self):
      data = {
        'size': 26214400
      }
      return data
      
    def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['autoescape'] = self.research_doc_autoescape()
      data['cycle'] = self.research_doc_cycle()
      data['cycle_color'] = self.research_doc_cycle_color()
      data['filter_add'] = self.research_doc_filter_add()
      data['filter_date'] = self.research_doc_filter_date()
      data['colors'] = self.dict_color()
      data['colors_none'] = self.dict_none_color()
      data['dict_cars'] = self.dict_sort()
      data['escapejs'] = self.escapejs()
      data['filesizeformat'] = self.filesizeformat()
      return data