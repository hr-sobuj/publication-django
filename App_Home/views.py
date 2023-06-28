from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    if request.method=='POST':
        search=request.POST.get('search')
        book=Book.objects.filter(book_title__icontains=search)
        writer=Book.objects.filter(writer__icontains=search)
        search_book=None
        if(len(book)):
            search_book=book 
        if(len(writer)):
            search_book=writer 

        if(search_book is None):
            search_book=None

        # print(book)
        dict={
            'title':'Home',
            'books':search_book,
        }
        return render(request, 'App_Home/search.html', context=dict)
    books=Book.objects.all()
    # print(books)
    dict={
        'title':'Home',
        'books':books,
    }
    return render(request, 'App_Home/index.html', context=dict)

def details(request,pk):
    if request.method=='POST':
        search=request.POST.get('search')
        book=Book.objects.filter(book_title__icontains=search)
        writer=Book.objects.filter(writer__icontains=search)
        if(len(book)):
            search_book=book 
        if(len(writer)):
            search_book=writer 

        if(search_book is None):
            search_book=None

        # print(book)
        dict={
            'title':'Home',
            'books':search_book,
        }
        return render(request, 'App_Home/search.html', context=dict)
    try:
        book=get_object_or_404(Book, pk=pk)
        books=Book.objects.all()
    except Book.DoesNotExist:
        book = None
        books = None
    book=Book.objects.get(pk=pk)
    books=Book.objects.all()
    dict={
        'book':book,
        'books':books,
    }
    return render(request, 'App_Home/details.html', context=dict)


def Books(request):
    if request.method=='POST':
        search=request.POST.get('search')
        book=Book.objects.filter(book_title__icontains=search)
        writer=Book.objects.filter(writer__icontains=search)
        search_book=None
        if(len(book)):
            search_book=book 
        if(len(writer)):
            search_book=writer 

        if(search_book is None):
            search_book=None

        # print(book)
        dict={
            'title':'Home',
            'books':search_book,
        }
        return render(request, 'App_Home/search.html', context=dict)
    books=Book.objects.all()
    # print(books)
    dict={
        'title':'Home',
        'books':books,
    }
    return render(request, 'App_Home/books.html', context=dict)
