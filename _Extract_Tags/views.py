from django.shortcuts import render
from django.contrib.auth.models import User
from _Extract_Tags.templatetags.utils.data_handle import DataHandle
from django.views.generic.base import TemplateView

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

class DataTable(TemplateView):
    template_name = "app/templatetags/table_demo.html"

    def _get_table_data(self, data):

      data_handle = DataHandle()
    
      table_data = {
        'options': {
          'table_id': 'table_advanced_demo'
        },
        'columns': {
          'username': data_handle.get_table_column_text(column_id='username', label="User Name"),
          'first_name': data_handle.get_table_column_text(column_id='first_name', label="First Name"),
          'last_name': data_handle.get_table_column_text(column_id='last_name', label="Last Name"),
          'email': data_handle.get_table_column_text(column_id='email', label="Email"),
          'is_staff': data_handle.get_table_column_text(column_id='is_staff', label="Staff"),
          'date_joined': data_handle.get_table_column_text(column_id='date_joined', label="Date Joined"),
        },
        'var_columns': {}
      }

      table_data = data_handle.convert_to_table_data(data, table_data)

      return table_data
    
    def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      users = User.objects.all()

      data['table_data'] = self._get_table_data(users)

      return data