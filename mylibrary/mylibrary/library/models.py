from django.db import models




class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_surname = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, default='asedfd')
    publication_year = models.PositiveIntegerField()
    page_count = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title} - {self.author_surname}"


class Reader(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"


class BookRent(models.Model):
    reader_surname = models.CharField(max_length=255)
    rent_date = models.DateField()
    book_title = models.CharField(max_length=255)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book_title} was rent to {self.reader_surname}: {self.rent_date} - {self.return_date}"
