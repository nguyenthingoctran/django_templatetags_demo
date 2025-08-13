from django.shortcuts import render

def index(request):
    context = {"val": 10}
    return render(request, "base/main_layout.html", context)