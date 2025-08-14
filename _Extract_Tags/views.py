from django.shortcuts import render
from django.contrib.auth.models import User
from _Extract_Tags.templatetags.utils.data_handle import DataHandle

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

class DataTable():
    def _get_table_data(self, post_data):

      data_handle = DataHandle()
    
      table_data = {
        'options': {
        },
        'columns': {
          'username': data_handle.get_table_column_text(column_id='username', label="User Name")
        }
      }

      table_data = data_handle.convert_to_table_data(users, table_data)

    def get_context_data(self, **kwargs):
      data = super().get_context_data()
      users = User.objects.all()

      data['table_data'] = self._get_table_data(users)

      return data