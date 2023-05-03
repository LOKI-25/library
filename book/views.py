from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Book
from .form import BookForm

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)|Book.objects.filter(category__icontains=query)
    else:
        books = Book.objects.all().order_by('title')
    paginator = Paginator(books, 2)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'index.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    return render(request, 'bookdetail.html', {'book': book})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'bookedit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookedit.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
