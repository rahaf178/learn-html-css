from django.shortcuts import render
from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name", "world")
    return HttpResponse(f"Hello, {name}")

def index2(request, val1):
    try:
        val1 = int(val1)
        return HttpResponse(f"value1 = {val1}")
    except:
        return HttpResponse("error, expected val1 to be integer")

    





