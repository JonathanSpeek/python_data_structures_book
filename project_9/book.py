class Book:
    def __init__(self, book_title, book_author):
        self.title = book_title
        self.author = book_author
        self.wait = []
        self.patron = ''

    def add_patron(self, patron_name):
        if self.patron == '':
            self.patron = patron_name
            patron_name.add_book(self.title)
        else:
            self.wait.append(patron_name)
