from django.views.generic.base import TemplateView
from datetime import datetime
from _Extract_Tags.data_hardcode.data_templatetag_filter import DataResearchTemplateTagFilter

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
      data['list_filter'] = DataResearchTemplateTagFilter().data_filter()
      return data