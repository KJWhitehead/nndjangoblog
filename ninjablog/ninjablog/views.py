from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, Homepage!")

def about(request):
    return HttpResponse("Hello, About!")