from research_doc import views

class DataResearchTemplateTagFilter():
  def data_filter(self):
    data = [
      {
        'filter_name': 'add',
        'description': 'Cộng/Bổ sung thêm vào',
        'id_modal': 'modalAdd',
        'modal': {
          'title': 'Filter - Add',
          'data': views.Research_Doc().research_doc_filter_add(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/add.html'
        }
      },{
        'filter_name': 'addslashes',
        'description': "Thêm ký tự gạch chéo (\) trước bất kỳ dấu nháy (') nào.",
        'id_modal': 'modalAddslashes',
        'modal': {
          'title': 'Filter - Addslashes',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/addslashes.html'
        }
      },{
        'filter_name': 'capfirst',
        'description': "Trả về chữ cái đầu tiên ở dạng in hoa",
        'id_modal': 'modalCapfirst',
        'modal': {
          'title': 'Filter - Capfirst',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/capfirst.html'
        }
      },{
        'filter_name': 'center',
        'description': "Căn giữa text theo chiều rộng chỉ định.",
        'id_modal': 'modalCenter',
        'modal': {
          'title': 'Filter - Center',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/center.html'
        }
      },{
        'filter_name': 'cut',
        'description': "Xoá bất kỳ ký tự hoặc cụm từ nào được chỉ định.",
        'id_modal': 'modalCut',
        'modal': {
          'title': 'Filter - Cut',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/cut.html'
        }
      },{
        'filter_name': 'date',
        'description': "Trả về ngày tháng theo format đã chỉ định.",
        'id_modal': 'modalDate',
        'modal': {
          'title': 'Filter - Date',
          'data': views.Research_Doc().research_doc_filter_date(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/date.html'
        }
      },{
        'filter_name': 'default',
        'description': "Trả về giá trị cụ thể nếu giá trị là False",
        'id_modal': 'modalDefault',
        'modal': {
          'title': 'Filter - Default',
          'data': views.Research_Doc().dict_color(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/default.html'
        }
      },{
        'filter_name': 'default_if_none',
        'description': "Trả về giá trị cụ thể nếu giá trị là None",
        'id_modal': 'modalDefaultIfNone',
        'modal': {
          'title': 'Filter - Default If None',
          'data': views.Research_Doc().dict_none_color(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/default_if_none.html'
        }
      },{
        'filter_name': 'dictsort',
        'description': "Sắp xếp xếp 1 dict bởi giá trị cho trước",
        'id_modal': 'modalDictsort',
        'modal': {
          'title': 'Filter - Dictsort',
          'data': views.Research_Doc().dict_sort(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/dictsort.html'
        }
      },{
        'filter_name': 'dictsortreversed',
        'description': "Sắp xếp một dict theo chiều ngược lại, theo giá trị đã cho.",
        'id_modal': 'modalDictsortreversed',
        'modal': {
          'title': 'Filter - Dictsortreversed',
          'data': views.Research_Doc().dict_sort(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/dictsortreversed.html'
        }
      },{
        'filter_name': 'divisibleby',
        'description': "Trả về True nếu giá trị có thể chia cho số được chỉ đinh, nếu không thì trả về False",
        'id_modal': 'modalDivisibleby',
        'modal': {
          'title': 'Filter - Divisibleby',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/divisibleby.html'
        }
      },{
        'filter_name': 'escape',
        'description': "Thoát mã HTML khỏi chuỗi",
        'id_modal': 'modalEscape',
        'modal': {
          'title': 'Filter - Escape',
          'data': views.Research_Doc().research_doc_autoescape(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/escape.html'
        }
      },{
        'filter_name': 'escapejs',
        'description': "Thoát mã JS khỏi chuỗi",
        'id_modal': 'modalEscapejs',
        'modal': {
          'title': 'Filter - Escapejs',
          'data': views.Research_Doc().escapejs(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/escapejs.html'
        }
      },{
        'filter_name': 'filesizeformat',
        'description': "Trả về file size format",
        'id_modal': 'modalFilesizeformat',
        'modal': {
          'title': 'Filter - Filesizeformat',
          'data': views.Research_Doc().filesizeformat(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/filesizeformat.html'
        }
      },{
        'filter_name': 'first',
        'description': "Trả về phần tử đầu tiên trong 1 object",
        'id_modal': 'modalFirst',
        'modal': {
          'title': 'Filter - modalFirst',
          'data': views.Research_Doc().dict_color(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/first.html'
        }
      },{
        'filter_name': 'floatformat',
        'description': "Làm tròn số thập phân được chỉ định, mặc định là một số thập phân",
        'id_modal': 'modalFloatformat',
        'modal': {
          'title': 'Filter - Floatformat',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/floatformat.html'
        }
      },{
        'filter_name': 'force_escape',
        'description': "Thoát mã HTML từ 1 string",
        'id_modal': 'modalForceEscape',
        'modal': {
          'title': 'Filter - Force Escape',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/force_escape.html'
        }
      },{
        'filter_name': 'get_digit',
        'description': "Trả về chữ số cụ thể của một số.",
        'id_modal': 'modalGetDigit',
        'modal': {
          'title': 'Filter - Get Digit',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/get_digit.html'
        }
      },{
        'filter_name': 'iriencode',
        'description': "Chuyển IRI thành URL",
        'id_modal': 'modalIriencode',
        'modal': {
          'title': 'Filter - Iriencode',
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/iriencode.html'
        }
      },{
        'filter_name': 'join',
        'description': "Nối các element của một list thành một chuỗi",
        'id_modal': 'modalJoin',
        'modal': {
          'title': 'Filter - Join',
          'data': views.Research_Doc().research_doc_cycle(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/join.html'
        }
      },{
        'filter_name': 'json_script',
        'description': "Trả về chuỗi object thành chuỗi JSON",
        'id_modal': 'modalJsonScript',
        'modal': {
          'title': 'Filter - Json Script',
          'data': views.Research_Doc().dict_sort(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/json_script.html'
        }
      },{
        'filter_name': 'last',
        'description': "Trả về phần tử cuối cùng của một Object",
        'id_modal': 'modalLast',
        'modal': {
          'title': 'Filter - Last',
          'data': views.Research_Doc().research_doc_cycle(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/last.html'
        }
      },{
        'filter_name': 'length',
        'description': "Trả về số lượng item của một Object, số lượng ký tự trong một String",
        'id_modal': 'modalLength',
        'modal': {
          'title': 'Filter - Length',
          'data': views.Research_Doc().research_doc_cycle(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/length.html'
        }
      },{
        'filter_name': 'linebreaks',
        'description': "Trả về text với thẻ <br/> thay thế cho xuống dòng, và thẻ <p> bao quanh 1 dòng",
        'id_modal': 'modalLinebreaks',
        'modal': {
          'title': 'Filter - Line Breaks',
          'data': views.Research_Doc().text_1(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/linebreaks.html'
        }
      },{
        'filter_name': 'linebreaksbr',
        'description': "Trả về text với thẻ <br/> thay thế cho xuống dòng",
        'id_modal': 'modalLinebreaksBr',
        'modal': {
          'title': 'Filter - Line Breaks Br',
          'data': views.Research_Doc().text_1(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/linebreaksbr.html'
        }
      },{
        'filter_name': 'linenumbers',
        'description': "Trả về text và số đếm mỗi dòng.",
        'id_modal': 'modalLinenumbers',
        'modal': {
          'title': 'Filter - Line Numbers',
          'data': views.Research_Doc().text_1(),
          'template_name': 'app/research_doc/template_tags_and_filter/content_templatetags_and_filter/filter_modal/linenumbers.html'
        }
      }
    ]
    return data