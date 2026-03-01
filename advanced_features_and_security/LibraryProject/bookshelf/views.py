from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookSearchForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure book listing view.
    Uses Django ORM to prevent SQL injection.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
@csrf_protect
def create_book(request):
    """
    Secure book creation view.
    CSRF protection enabled.
    """
    if request.method == "POST":
        title = request.POST.get("title", "")
        author = request.POST.get("author", "")

        # Basic validation
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('book_list')

    return render(request, 'bookshelf/form_example.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """
    Secure edit view using get_object_or_404 to prevent tampering.
    """
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You have permission to EDIT {book.title}")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """
    Secure delete view using ORM safely.
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse("Book deleted successfully.")


def search_books(request):
    """
    Secure search functionality using Django forms
    to validate and sanitize user input.
    """
    form = BookSearchForm(request.GET)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('q')
        if query:
            # Safe ORM filtering (prevents SQL injection)
            books = books.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })