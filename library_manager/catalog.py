# library_manager/catalog.py
from .utils.data_validation import validate_book_data

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        book_data = {'title': title, 'author': author, 'genre': genre}
        if validate_book_data(book_data):
            self.books.append(book_data)
        else:
            raise ValueError("Invalid book data")

    def remove_book(self, title):
        self.books = [book for book in self.books if book['title'] != title]

    def find_books_by_title(self, title):
        return [book for book in self.books if book['title'] == title]

    def find_books_by_author(self, author):
        return [book for book in self.books if book['author'] == author]

    def find_books_by_genre(self, genre):
        return [book for book in self.books if book['genre'] == genre]

    def view_all_books(self):
        return self.books