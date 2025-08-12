from django.shortcuts import render

def index(request):
    context = {"val": 10}
    return render(request, "base/index.html", context)

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")