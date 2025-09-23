from django.views.generic.base import TemplateView
from datetime import datetime
from _Extract_Tags.data_hardcode.data_templatetag_filter import DataResearchTemplateTagFilter
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.shortcuts import render
from research_doc.data.list_object import ListObjectResearch
from research_doc.data.list_array import ListArrayResearch

# Create your views here.
class Django_Templatetags(TemplateView):
    template_name = "app/research_doc/template_tags_and_filter/index.html"

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
    
    def text_1(self):
      data = 'Hello\nmy name is Leo.\n\nI am a student.'
      return data
    
    def text_2(self):
      data = '<h1>Hello, Kitty</h1>'
      return data

    def text_3(self):
      data = '_Hi, my name is Linus\n Hello - Kitty__Hihi-'
      return data
    
    def object_1(self):
      data = [
        "Plain text item.",
        format_html("<strong>Bold item</strong> with HTML."),
        "Hello, Kitty",
        format_html("<em>Emphasized item</em>.")
      ]
      return data
    
    def number_1(self):
      data = {
        "1": 1234.5678,
        '2': 10
      } 
      return data
    
    def date_list_1(self):
      data = {
        'mybirthdate': datetime(1994, 4, 28),   
        'mydate': datetime(2020, 10, 17),
        'date1': datetime(2022, 6, 8, 9, 30),  
        'date2': datetime(2022, 6, 8, 13, 45),
        'marslanding': datetime(2050, 5, 17),
        'moonlanding': datetime(1969, 7, 20),
        'date3': datetime(2022, 6, 8, 17, 39),
        'date4': datetime(2022, 6, 8, 8, 13)
      }
      return data
        
    def pluralize(self):
      data = [0, 1, 2]
      return data
    
    def firstof(self):
      firstof = [0, "", 'Hello', 'Kitty']
      return firstof
    
    def firstof_1(self):
      firstof_1 = [0, "", 0]
      return firstof_1
    
    def get_user_list(self):
      users = User.objects.all()
      return users
    
    def get_user(self):
      users = User.objects.all()
      user = users[0]
      return user
    
    def athlete_list(self):
      athlete_list = []
      return athlete_list
    
    def coach_list(self):
      coach_list = []
      return coach_list
    
    def cheerleader_list(self):
      cheerleader_list = ['tran', 'thao']
      return cheerleader_list
    
    def mycar(self):
      mycar = {
        'car1': {
          'brand': 'Ford',
          'model': 'Mustang',
          'year': '1964'
        }
      }
      return mycar
    
    def somevar(self):
      somevar = 'hello'
      return somevar
    
    def messages(self):
      messages = [
        'All of the above can be combined to form complex expressions.',
        'For such expressions',
        'That is, the precedence rules',
        'The precedence of the operators',
      ]
      return messages
    
    def language_program_list(self):
      value = ['Python', 'Python', 'Python', 'Ruby', 'Java', 'Java', 'Javascript', 'Javascript']
      return value
    
    def coder_list(self):
      coder_list = [
        {'name': 'Nguyen', 'language': 'Python'},
        {'name': 'Thi', 'language': 'Ruby'},
        {'name': 'Ngoc', 'language': 'JS'},
        {'name': 'Ngoc', 'language': 'C++'},
        {'name': 'Ngoc', 'language': 'Python'},
        {'name': 'Tran', 'language': 'C++'},
      ]
      return coder_list
    
    def coder_list_2(self):
      coder_list = [
        {
          'name': 'Nguyen', 
          'language': {
            'lang_name': "Python",
            'framework': 'Django'
          }
        },{
          'name': 'Ngoc', 
          'language': {
            'lang_name': 'Python',
            'framework': 'Laravel'
          }
        },{
          'name': 'Thi', 
          'language': {
            'lang_name': 'Ruby',
            'framework': 'Wript'
          }
        },{
          'name': 'Ngoc', 
          'language': {
            'lang_name': 'JS',
            'framework': 'Jquery'
          }
        },{
          'name': 'Ngoc', 
          'language': {
            'lang_name': 'C++',
            'framework': 'Nope'
          }
        },{
          'name': 'Tran', 
          'language': {
            'lang_name': 'JS',
            'framework': 'Nope'
          }
        },{
          'name': 'Tran', 
          'language': {
            'lang_name': 'Python',
            'framework': 'Laravel'
          }
        }
      ]
      return coder_list

    def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['list_filter'] = DataResearchTemplateTagFilter().data_filter()
      data['autoescape'] = self.research_doc_autoescape()
      data['cycle'] = self.research_doc_cycle()
      data['firstof'] = self.firstof()
      data['firstof_1'] = self.firstof_1()
      data['fruits'] = self.research_doc_cycle()
      data['cars'] = self.dict_sort()
      data['users'] = self.get_user_list()
      data['athlete_list'] = self.athlete_list()
      data['mycar'] = self.mycar()
      data['two_loop'] = self.research_doc_filter_add()
      data['coach_list'] = self.coach_list()
      data['somevar'] = self.somevar()
      data['myinfo'] = self.get_user()
      data['messages'] = self.messages()
      data['language_program_list'] = self.language_program_list()
      data['coder_list'] = self.coder_list()
      data['page'] = 1
      data['coder_list_2'] = self.coder_list_2()
      return data
    
class Javascript(TemplateView):
  template_name = 'app/research_doc/javascript/index.html'

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['object_list'] = ListObjectResearch().data_object()
    data['static_method'] = ListObjectResearch().data_static_methods()
    data['array_list'] = ListArrayResearch().data_array()
    return data