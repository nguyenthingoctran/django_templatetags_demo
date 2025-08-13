from django.shortcuts import render

def index(request):
    context = {"val": 10}
    return render(request, "base/main_layout.html", context)

def table_demo(request):
    data = {"data": 10}
    return render(request, "app/templatetags/table_demo.html")