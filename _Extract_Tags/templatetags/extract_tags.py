from django import template

register = template.Library()

@register.inclusion_tag('app/templatetags/tags/title/main_title.html')
def main_title(value="", className=""):
  data = {
    "value": value,
    "className": className
  }
  return data

@register.inclusion_tag('app/templatetags/tags/breadcrumb/breadcrumb.html')
def breadcrumb(breadcrumb_list=[]):
  data = {
    'breadcrumb_list': breadcrumb_list
  }
  return data

@register.inclusion_tag('app/templatetags/tags/modal/modal.html')
def modal(id="", title="", data=None, backdrop="static", template_name=""):
  data = {
    'id': id,
    'title': title,
    'data': data,
    'backdrop': backdrop,
    'template_name': template_name
  }
  return data

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