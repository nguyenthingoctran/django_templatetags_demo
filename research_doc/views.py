from django.views.generic.base import TemplateView

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
      
    def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['autoescape'] = self.research_doc_autoescape()
      data['cycle'] = self.research_doc_cycle()
      data['cycle_color'] = self.research_doc_cycle_color()
      data['filter_add'] = self.research_doc_filter_add()
      return data