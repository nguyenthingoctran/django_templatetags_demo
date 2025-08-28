from django.shortcuts import render
from django.contrib.auth.models import User
from _Extract_Tags.templatetags.utils.data_handle import DataHandle
from django.views.generic.base import TemplateView
from _Extract_Tags.data_hardcode.data_table import DataTableHardCode
from django.urls import reverse

def index(request):
    context = {"val": 10}
    return render(request, "base/main_layout.html", context)

def table_demo(request):
    users = User.objects.all()

    for user in users:
        print (user.__dict__, "123")

    data = {
        'users': users
    }
    
    return render(request, "app/templatetags/table_demo.html", data)

class ListGuide(TemplateView):
  template_name = "app/templatetags_guide/index_guide.html"

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    return data
  
class Title(TemplateView):
  template_name = "app/templatetags_guide/title/index.html"

  def get_data_breadcrumbs(self):
    breadcrumb_data = [
        {
          'label': 'Home',
          'url': reverse("Screen:home")
        },
        {
          'label': 'Template Tags Guide',
          'url': reverse("_Extract_Tag:list_guide")
        },
        {
          'label': 'Title'
        }
    ]
    return breadcrumb_data

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['breadcrumb_data'] = self.get_data_breadcrumbs()
    return data
  
class Breadcrumbs(TemplateView):
  template_name = "app/templatetags_guide/breadcrumbs/index.html"

  def get_data_breadcrumbs(self):
    breadcrumb_data = [
        {
          'label': 'Home',
          'url': reverse("Screen:home")
        },
        {
          'label': 'Template Tags Guide',
          'url': reverse("_Extract_Tag:list_guide")
        },
        {
          'label': 'Breadcrumbs'
        }
    ]
    return breadcrumb_data

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['breadcrumb_data'] = self.get_data_breadcrumbs()
    return data
  
class Modals(TemplateView):
  template_name = "app/templatetags_guide/modals/index.html"

  def get_data_breadcrumbs(self):
    breadcrumb_data = [
        {
          'label': 'Home',
          'url': reverse("Screen:home")
        },
        {
          'label': 'Template Tags Guide',
          'url': reverse("_Extract_Tag:list_guide")
        },
        {
          'label': 'Modals'
        }
    ]
    return breadcrumb_data
  
  def data_modals(self):
    dict_cars = {
      'cars': [
        {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
        {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
        {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
        {'brand': 'Ford', 'model': 'Focus', 'year': 2004}
      ]
    }
    return dict_cars

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['breadcrumb_data'] = self.get_data_breadcrumbs()
    data['data_modals'] = self.data_modals()
    return data

class DataTable(TemplateView):
    template_name = "app/templatetags/table_demo.html"

    def _get_table_data(self, data):

      data_handle = DataHandle()
    
      table_data = {
        'options': {
          'table_id': 'table_advanced_demo'
        },
        'columns': {
          'id': data_handle.get_table_column_text(column_id='id', label="ID"),
          'username': data_handle.get_table_column_text(column_id='username', label="User Name"),
          'first_name': data_handle.get_table_column_text(column_id='first_name', label="First Name"),
          'last_name': data_handle.get_table_column_text(column_id='last_name', label="Last Name"),
          'email': data_handle.get_table_column_text(column_id='email', label="Email"),
          'is_staff': data_handle.get_table_column_text(column_id='is_staff', label="Staff"),
          'date_joined': data_handle.get_table_column_text(column_id='date_joined', label="Date Joined"),
          'password': data_handle.get_table_column_text(column_id='password', label="Password"),
          'last_login': data_handle.get_table_column_text(column_id='last_login', label="Last Login"),
          'is_superuser': data_handle.get_table_column_text(column_id='is_superuser', label="Is Super Users"),

        },
        'var_columns': {}
      }

      table_data = data_handle.convert_to_table_data(data, table_data)

      return table_data
    
    def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      users = User.objects.all()

      for u in users:
        print(u.__dict__)

      data_column = DataTableHardCode().data_table()

      data['table_data'] = self._get_table_data(users)

      return data
    
class Alert(TemplateView):
  template_name = "app/templatetags_guide/alert/index.html"

  def get_data_breadcrumbs(self):
    breadcrumb_data = [
        {
          'label': 'Home',
          'url': reverse("Screen:home")
        },
        {
          'label': 'Template Tags Guide',
          'url': reverse("_Extract_Tag:list_guide")
        },
        {
          'label': 'Alert'
        }
    ]
    return breadcrumb_data

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    data['breadcrumb_data'] = self.get_data_breadcrumbs()
    return data