# sandbox environment for testing purposes

from Book import Book
from Owner import Owner

mr_smee = Owner("Mr. Smee")
jungle = Book("The Jungle", "Upton Sinclair")
moby = Book("Moby Dick", "Herman Melville")

mr_smee.add_a_book(jungle)
mr_smee.add_a_book(moby)

moby.set_owner(mr_smee)
jungle.owner = mr_smee # jungle.set_owner(mr_smee)

print(jungle.owner)

# print(moby.owner.name)

# for book in mr_smee.books:
#     print(book)
#     print(book.title)