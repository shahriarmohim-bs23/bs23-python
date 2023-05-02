from django.urls import path

from .import views
from .views import AddItemView,BookAddedView,AllBooksView, BorrowedCopyView, OwnedCopyView,BorrowCopyView,BookDetailView
from .forms import BookForm, CategoryForm,CopyForm
app_name = 'library'
urlpatterns = [
    path('add/book/', AddItemView.as_view(form_class=BookForm,template_name='pages/add_book.html'), name='add_book'),
    path('add/category/', AddItemView.as_view(form_class=CategoryForm,template_name='pages/add_category.html'), name='add_category'),
    path('add/copy/', AddItemView.as_view(form_class=CopyForm, template_name='pages/add_copy.html'), name='add_copy'),
    path('book_added/', BookAddedView.as_view(), name='book_added'),
    path('view_all_book/', AllBooksView.as_view(), name='all_books'),
    path('owned/copy/', OwnedCopyView.as_view(), name='owned_books'),
    path('borrowed/copy/', BorrowedCopyView.as_view(), name='borrowed_books'),
    path('category/<slug:category_slug>/', AllBooksView.as_view(), name='category_list'),
    path('borrow/<slug:slug>/', BorrowCopyView.as_view(), name='borrow_copy'),
    path('item/<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('searchbooks/', views.search_books, name='search_books'),

]
