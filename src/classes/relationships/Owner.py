class Owner():

    def __init__(self, name):
        self._name = name

        # initialize a list of books owned by self
        self._books = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # add a book to the owner's list of books
    def get_books(self):
        return self._books
    
    def add_a_book(self, book):
        from Book import Book
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise Exception("Book must be an instance of class Book!")
        
    books = property(get_books, add_a_book)