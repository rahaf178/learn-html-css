from django.shortcuts import render
from django.shortcuts import render 

def index(request): 
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")    





