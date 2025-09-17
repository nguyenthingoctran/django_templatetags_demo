class ListObjectResearch():
  def data_object(self):
    data = [
      {
        'data_bs_target': 'constructor',
        'name': 'Constructor',
        'include_template': 'app/research_doc/javascript/list_js_content/object/constructor.html',
      }
    ]
    return data
  
  def data_static_methods(self):
    data = [
      {
        'data_bs_target': 'st_assign',
        'name': 'assign()',
        'include_template': 'app/research_doc/javascript/list_js_content/object/assign.html',
      },
      {
        'data_bs_target': 'st_create',
        'name': 'create()',
        'include_template': 'app/research_doc/javascript/list_js_content/object/create.html',
      },
      {
        'data_bs_target': 'st_defineProperties',
        'name': 'defineProperties()',
        'include_template': 'app/research_doc/javascript/list_js_content/object/define_properties.html',
      }
    ]
    return data