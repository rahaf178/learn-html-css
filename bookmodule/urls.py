from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('books/html5/links', views.html5_links, name='html5_links'),
    path('books/html5/text/formatting', views.text_formatting, name='text_formatting'),
    path('books/html5/listing', views.listing, name='listing'), 
    path('books/html5/tables', views.tables, name='tables'),
    path('books/search', views.search_books, name='search_page'),
    path('books/results', views.search_result, name='search_results')
]