from django.shortcuts import render

# Create your views here.
def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')