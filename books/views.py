from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book, Review
from django.db.models import Q
from .forms import AddBook, AddReview
from django.shortcuts import render, redirect

class BookListView(
    # LoginRequiredMixin, 
    ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(
#        LoginRequiredMixin, 
#        PermissionRequiredMixin,
        DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    # permission_required = 'special_status'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

def add_book(request):
    """ Add a Book """

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddBook()
    else:
        # Post data submitted, process data
        form = AddBook(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/books/')
    # Display a blank or invalid form
    context = {'form': form}
    # template_name = 'books/new_book.html'
    return render(request, 'books/add_book.html', context)

def edit_book(request, book_id):
    """ Edit a Book """

    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddBook(instance=book)
    else:
        # Post data submitted, process data
        form = AddBook(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    # Display a blank or invalid form
    context = {'book': book, 'form': form}
    # template_name = 'books/new_book.html'
    return render(request, 'books/edit_book.html', context)
    
def delete_book(request, book_id):
    """ Delete a Book """
    book = Book.objects.get(id=book_id)
    Book.objects.get(id=book_id).delete()

    context = {'deleted_book': book}
    return render(request, 'books/book_list.html', context)

def add_review(request):
    """ Add a Review """

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddReview()
    else:
        # Post data submitted, process data
        form = AddReview(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/books/')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'books/add_review.html', context)

def delete_review(request, review_id):
    """ Delete a Review """
    review = Review.objects.get(id=review_id)
    Review.objects.get(id=review_id).delete()

    context = {'deleted_review': review}
    return render(request, 'books/book_list.html', context)