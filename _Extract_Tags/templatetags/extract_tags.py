from django import template

register = template.Library()

@register.inclusion_tag('app/templatetags/tag/data_table.html')
def data_table(data_table):
  data_table = {
    '1': "hello",
    '2': "Kitty"
  }
  return {'data': data_table}