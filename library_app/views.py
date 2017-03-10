from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .models import Present_Book, Request_Book
from .readxml import get_data
from django.utils import timezone


class AccountCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'library_app/signup.html'
    def get_success_url(self):
        return reverse('library_app:login')

@method_decorator(login_required, name='dispatch')
class RequestIndexView(generic.ListView):
    template_name = 'library_app/request_index.html'
    context_object_name = 'latest_request_book_list'
    model = Request_Book

    def get_queryset(self):
        return Request_Book.objects.order_by('-time')[:50]

@method_decorator(login_required, name='dispatch')
class PresentIndexView(generic.ListView):
    template_name = 'library_app/present_index.html'
    context_object_name = 'latest_present_book_list'
    model = Present_Book

    def get_queryset(self):
        return Present_Book.objects.order_by('-time')[:50]

class DetailView(generic.DetailView):
    model = User
    template_name = 'library_app/detail.html'

@csrf_protect
def request_page(request):
    context = {}
    return render(request, 'library_app/request_book.html', context)

def present_page(request):
    context = {}
    return render(request, 'library_app/present_book.html', context)

@csrf_protect
def search_isbn_request(request):
    isbn = request.POST["isbn"]
    try:
        book_data = get_data(isbn, 'isbn')
        context = book_data
        return render(request, 'library_app/search_result_request.html', context)
    except:
        error_massage = 'Can not find'
        return render(request, 'library_app/request_book.html', {'error_massage': error_massage})

def search_isbn_present(request):
    isbn = request.POST["isbn"]
    try:
        book_data = get_data(isbn, 'isbn')
        context = book_data
        return render(request, 'library_app/search_result_present.html', context)
    except:
        error_massage = 'Can not find'
        return render(request, 'library_app/present_book.html', {'error_massage': error_massage})

@csrf_protect
def search_title(request):
    isbn = request.POST["isbn"]
    try:
        book_data = get_data(isbn, 'title')
        context = book_data
        return render(request, 'library_app/search_result', context)
    except:
        return render(request, 'library_app/search_page', {'error_massage': 'Can not find'})

def regist_request(request):
    user = request.user
    req_book = Request_Book(
                   title = request.POST['title'],
                   author = request.POST['author'],
                   book_link = request.POST['link'],
                   isbn = request.POST['isbn'],
                   user = user,
                   time = timezone.now()
                   )
    req_book.save()
    return redirect("library_app:request_index")

def regist_present(request):
    user = request.user
    prs_book = Present_Book(
                   title = request.POST['title'],
                   author = request.POST['author'],
                   book_link = request.POST['link'],
                   isbn = request.POST['isbn'],
                   user = user,
                   time = timezone.now()
                   )
    prs_book.save()
    return redirect("library_app:index")

def request_delete(request):
    book_id = request.POST["id"]
    target_book = Request_Book.objects.get(pk=book_id)
    user_id = target_book.user_id
    if request.user.id == user_id:
        target_book = Request_Book.objects.get(pk=book_id)
        target_book.delete()
    else:
        print("missmatch")
    return redirect("library_app:index")







# Create your views here.
