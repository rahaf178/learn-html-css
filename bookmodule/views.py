from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Student
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Count

def index(request):
    name = request.GET.get("name", "world")
    return HttpResponse(f"Hello, {name}")

def index2(request, val1):
    try:
        val1 = int(val1)
        return HttpResponse(f"value1 = {val1}")
    except:
        return HttpResponse("error, expected val1 to be integer")

    
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

def text_formatting(request):
    return render(request, 'bookmodule/html5_text_formatting.html')

def listing(request):
    return render(request, 'bookmodule/html5_listing.html')

def tables(request):
    return render(request, 'bookmodule/html5_tables.html')

def add_book(request):
    Book.objects.create(
        title='Continuous Delivery',
        author='J.Humble and D. Farley',
        edition=1
    )
    return HttpResponse("Book added")

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains=' and ') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if mybooks.exists():
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def book_list_task1(request):
    books = Book.objects.filter(price__lte=80)
    return render(request, 'bookmodule/books_task1.html', {'books': books})

def book_list_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/books_task2.html', {'books': books})

def book_list_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & 
        (~Q(title__icontains='co') | ~Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/books_task3.html', {'books': books})

def book_list_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/books_task4.html', {'books': books})

def book_list_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    return render(request, 'bookmodule/books_stats.html', {'stats': stats})

def students_per_city(request):
    data = Student.objects.values('address__city').annotate(
        total=Count('id')
    )

    return render(request, 'bookmodule/students_city.html', {'data': data})