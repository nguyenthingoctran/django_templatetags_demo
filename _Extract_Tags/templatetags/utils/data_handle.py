class DataHandle():
  def convert_to_table_data(self, objects, table_data):
    #1) Set giá trị cho từng column
    for key in table_data['columns'].keys():
      table_data['columns'][key]['values'] = self.get_object_column_values(objects, key)

    #2) Set giá trị cho từng val column
    for key in table_data['var_columns'].keys():
      table_data['var_columns'][key]['values'] = self.get_object_column_values(objects, key)

    table_data['total'] = [i for i in range(len(objects))]
    return table_data

  def _get_table_column_base(self, column_id, label='', width=-1, align="left"):
    column = {
      'setting': {
        'label': label if label != '' else column_id,
        'width': width,
        'align': align
      }
    }
    return column

  def get_table_column_text(self, column_id, label='', width=-1, align="left"):
    column = self._get_table_column_base(column_id, label, width, align) 
    return column