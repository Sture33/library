from django.shortcuts import render
from library1.models import Book, Reader, BookRent


# Create your views here.
def show_start_page(request):
    return render(request, "index.html")


def show_showbooks_page(request):
    context = {"books": Book.objects.all()}

    return render(request, "showBooks.html", context=context)

def show_showreaders_page(request):
    context = {'readers': Reader.objects.all()}
    return render(request, "Readers.html", context=context)

def show_showrents_page(request):
    context = {'rents': BookRent.objects.all()}
    return render(request, "Rents.html", context=context)

def show_addbook_page(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("book_author_surname")
        genre = request.POST.get("book_genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count")
        description = request.POST.get("description")
        Book.objects.create(title=book_title,
                               author_name=author_name,
                               author_surname=author_surname,
                               genre=genre,
                               publication_year=publication_year,
                               page_count=page_count,
                               description=description)

    return render(request, "addBook.html")


def show_addreader_page(request):
    if request.method == "POST":
        name = request.POST.get("reader_name")
        surname = request.POST.get("reader_surname")
        age = request.POST.get("reader_age")
        address = request.POST.get("reader_address")

        Reader.objects.create(name=name,
                               surname=surname,
                               age=age,
                               address=address)

    return render(request, "addReader.html")
def show_addrent_page(request):
    if request.method == "POST":
        reader = request.POST.get("reader_surname")
        rent_date = request.POST.get("rent_date")
        title = request.POST.get("book_title")
        return_date = request.POST.get("return_date")

        BookRent.objects.create(reader_surname=reader,
                                rent_date=rent_date,
                                book_title=title,
                                return_date=return_date)

    return render(request, "addRent.html")
def show_deletebook_page(request):
    context = {"books": Book.objects.all()}
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        Book.objects.get(title=book_name).delete()
    return render(request, "delBook.html", context=context)
def show_deletereader_page(request):
    context = {"books": Reader.objects.all()}
    if request.method == 'POST':
        reader_name = request.POST.get('reader_name')
        Reader.objects.get(surname=reader_name).delete()
    return render(request, "delReader.html", context=context)
def show_deleterent_page(request):
    context = {"books": BookRent.objects.all()}
    if request.method == 'POST':
        reader_surname = request.POST.get('rent_name')
        BookRent.objects.get(reader_surname=reader_surname).delete()
    return render(request, "delRent.html", context=context)


def updateBook(request, pk):

    book = Book.objects.get(pk=pk)
    context = {'book': book}

    if request.method == 'POST':
        book.title = request.POST.get("book_title")
        book.author_name = request.POST.get("book_author_name")
        book.author_surname = request.POST.get("book_author_surname")
        book.genre = request.POST.get("book_genre")
        book.publication_year = request.POST.get("publication_year")
        book.page_count = request.POST.get("page_count")
        book.description = request.POST.get("description")
        book.save()

    return render(request, 'updateBook.html', context=context)

