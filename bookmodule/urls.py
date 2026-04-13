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
    path('books/simple/query', views.simple_query, name='simple_query'),
    path('books/complex/query', views.complex_query, name='complex_query'),
    path('books/lab8/task1/', views.book_list_task1, name='book_list_task1'),
    path('books/lab8/task2/', views.book_list_task2, name='book_list_task2'),
    path('books/lab8/task3/', views.book_list_task3, name='book_list_task3'),
    path('books/lab8/task4/', views.book_list_task4, name='book_list_task4'),
    path('books/lab8/task5/', views.book_list_task5, name='book_list_task5'),
    path('books/lab8/task6/', views.students_per_city, name='students_per_city'),

]
