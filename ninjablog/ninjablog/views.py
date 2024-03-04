from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello, Homepage!")
    return render(request, "index.html")
    

def about(request):
    # return HttpResponse("Hello, About!")
    return render(request, "about.html")