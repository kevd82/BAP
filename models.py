from django.db import models

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 1:
            errors["title"] = "Title cannot be blank!"
        if len(postData["description"]) < 1:
            errors["description"] = "Description cannot be blank!"
        return errors

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name must contain at least 2 characters!"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name must contain at least 2 characters!"
        if len(postData["notes"]) <5:
            errors["notes"] = "Notes must contain at least 5 characters!"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __str__(self):
        return "{}".format(self.title)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)