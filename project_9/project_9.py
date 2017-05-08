# A simple software system for a library models a library as a collection of books
# and patrons. A patron can have at most three books out on loan at any given time.
# A book also has a list of patrons waiting to borrow it. Each book has a title, an
# author, a patron to whom it has been checked out, and a list of patrons waiting for
# that book to be returned. Each patron has a name and the number of books it has
# currently checked out. Develop the classes Book and Patron to model these objects.
# Think first of the interface or set of methods used with each class, and then choose
# appropriate data structures for the state of the objects. Also, write a short script to
# test these classes.

from book import Book
from patron import Patron

book_1 = Book('1984', 'George Orwell')
book_2 = Book('Catch-22', 'Joseph Heller')
book_3 = Book('On the Road', 'Jack Kerouac')

patron_1 = Patron('Jonathan')
patron_2 = Patron('Susan')
patron_3 = Patron('Marisa')
patron_4 = Patron('Bill')
patron_5 = Patron('Michelle')
patron_6 = Patron('Steve')

book_1.add_patron(patron_1)
book_1.add_patron(patron_2)
book_2.add_patron(patron_1)
book_2.add_patron(patron_3)
book_2.add_patron(patron_4)
book_3.add_patron(patron_5)
book_3.add_patron(patron_6)

print('{name} has the following checked-out:'.format(name=patron_1.name))
for book in patron_1.books:
    print('{title}'.format(title=book))

print('{name} has the following checked-out:'.format(name=patron_2.name))
for book in patron_2.books:
    print('{title}'.format(title=book))

print('{name} has the following checked-out:'.format(name=patron_3.name))
for book in patron_3.books:
    print('{title}'.format(title=book))

print('{name} has the following checked-out:'.format(name=patron_4.name))
for book in patron_4.books:
    print('{title}'.format(title=book))

print('{name} has the following checked-out:'.format(name=patron_5.name))
for book in patron_5.books:
    print('{title}'.format(title=book))

print('{name} has the following checked-out:'.format(name=patron_6.name))
for book in patron_6.books:
    print('{title}'.format(title=book))
