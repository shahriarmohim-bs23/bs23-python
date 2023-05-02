from .models import Category, Book, Review, Copy, Borrow
from .forms import BookForm, CategoryForm, CopyForm
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .filter import FilterBooks
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views import View

def categories(request):
    return {
        'categories': Category.objects.all()
    }
class AddItemView(FormView):
    success_url = reverse_lazy('library:book_added')
    form_class = None

    def get_form_class(self):
        return self.form_class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def get_template_names(self):
        return [f'{self.template_name}']


    def form_valid(self, form):
        if isinstance(form, CopyForm):
            book = form.cleaned_data['book']
            qty = form.cleaned_data['copy']
            count = book.copies.count()

            for i in range(1, qty + 1):
                Copy.objects.create(book=book, copy=i + count, owner=self.request.user, status='available')
        else:
            form.save()
        return super().form_valid(form)
    

class BookAddedView(TemplateView):
    template_name = 'pages/book_added.html'

class PaginatedListView(ListView):
    paginate_by = 4
    context_object_name = 'data'

    def get_queryset(self):
        queryset = super().get_queryset()
        path = self.request.path
        if path == '/owned_copy/':
            return Copy.objects.filter(owner=self.request.user)
        elif path == '/borrowed_copy/':
            return Borrow.objects.filter(borrower=self.request.user)
        else:
            return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        paginator = Paginator(context[self.context_object_name], self.paginate_by)
        context[self.context_object_name] = paginator.get_page(page_number)
        return context



class AllBooksView(PaginatedListView):
    model = Book
    template_name = 'pages/view_book_list.html'
    context_object_name = 'products'
   

class BorrowedCopyView(PaginatedListView):
    model = Borrow
    template_name = 'pages/borrowed_copy.html'
    context_object_name = 'borrowed_copies'

class OwnedCopyView(PaginatedListView):
    model = Copy
    template_name = 'pages/owned_copy.html'
    context_object_name = 'owned_copies'



class BookDetailView(DetailView):
    model = Book
    template_name = 'pages/books/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.reviews.all()
        paginator = Paginator(reviews, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    def post(self, request, slug):
        book = self.get_object()
        content = request.POST.get('content', '')
        rating = request.POST.get('rating')
        if content:
            review = Review.objects.create(
                book=book,
                content=content,
                rating=rating,
                user=request.user
            )
            messages.success(request, 'Review added successfully!')
            return redirect('library:book_detail', slug=book.slug)
        else:
            messages.error(request, 'Review content cannot be empty!')
            return redirect('library:book_detail', slug=book.slug)
        
class BorrowCopyView(View):
    def get(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=slug)
        existing_borrow = Borrow.objects.filter(copy__book=book, borrower=request.user, return_date__isnull=True).first()
        if existing_borrow:
            messages.warning(request, "You have already borrowed a copy of this book.")
            return redirect('library:book_detail', slug=book.slug)

        for copy in book.copies.all():
            if copy.status == 'available':
                copy.status = 'borrowed'
                copy.save()
                Borrow.objects.create(copy=copy, borrower=request.user)
                messages.success(request, "Successfully borrowed the copy.")
                return redirect('library:book_detail', slug=book.slug)

        messages.warning(request, "There are no available copies.")
        return redirect('library:book_detail', slug=book.slug)











def search_books(request):
    books = Book.objects.all()
    filters = FilterBooks(request.GET, queryset=books)
    filtered_books = filters.qs
    return render(request, 'pages/books/searchbooks.html',
                  {'filters': filters, 'Books': filtered_books})