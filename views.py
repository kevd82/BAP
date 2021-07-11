from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author

def books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "book.html", context)

def create_book(request):
    author = Author.objects.author_validator(request.POST)

    if len(book) > 0:
        for key,value in book.items():
            messages.error(request, value)
        return redirect("/books")


    Book.objects.create(
        title = request.POST["title"],
        description = request.POST["description"])
    return redirect("/books")

def one_book(request, id):
    context = {
        "one_book": Book.objects.get(id=id),
        "authors": Author.objects.all()
    }
    return render(request, "show_book.html", context)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/books")

def add_author(request):
    this_book = Book.objects.get(id=request.POST["book"])
    this_author = Author.objects.get(id=request.POST["author"])

    this_book.authors.add(this_author)
    return redirect(f"/books/{this_book.id}")

def create_author(request):
    author = Author.objects.author_validator(request.POST)

    if len(author) > 0:
        for key,value in author.items():
            messages.error(request, value)
        return redirect("/authors")

    
    Author.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        notes=request.POST["notes"])
    return redirect("/authors")

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "author.html", context)

def one_author(request, id):
    context = {
        "one_author": Author.objects.get(id=id),
        "books": Book.objects.all()
    }
    return render(request, "show_author.html", context)

def add_book(request):
    this_book = Book.objects.get(id=request.POST["book"])
    this_author = Author.objects.get(id=request.POST["author"])

    this_author.books.add(this_book)
    return redirect(f"/authors/{this_author.id}")
