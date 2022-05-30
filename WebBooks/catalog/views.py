from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

# Create your views here.
def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = "на складе")
    # Здесь метод "all()" применён по умолчанию.
    num_instances_available = BookInstance.objects.all().count()
    # авторы книг
    num_authors = Author.objects.count()
    #num_genres = Genre.objects.count()
    #количество посещений этого views
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # Отрисовка Html-шаблона index.html с данными
    # Внутри переменной context
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           'num_visits' : num_visits},
                  )
