class Patron(object):
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title):
        self.books.append(title)