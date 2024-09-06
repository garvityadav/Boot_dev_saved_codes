class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name 
        self.books = []

    def add_book(self, book):
        self.books.append(Book(book.title,book.author))

    def remove_book(self, book):
        for target in self.books:
            if target.title == book.title and target.author==book.author:
                self.books.remove(target)
                break

    def search_books(self, search_string):
        query_result = []

        for book in self.books: 
            if search_string.lower() in book.author.lower() or search_string.lower() in book.title.lower():
                  query_result.append(book) 
        return query_result

