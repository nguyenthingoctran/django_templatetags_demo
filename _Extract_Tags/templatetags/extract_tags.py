from django import template

register = template.Library()

@register.inclusion_tag('app/templatetags/tags/table/table_advanced.html')
def table_advanced(data_table):
  data = {
    'data': data_table
  }
  return data

@register.inclusion_tag('app/templatetags/tags/table/td/text.html')
def table_td_text(data_column, row_index, key_column):
  value = data_column['values'][row_index]
  data = {
    'value': value
  }
  return data