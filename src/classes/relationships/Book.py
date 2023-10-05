class Book:

    def __init__(self, title, author):
        self._title = title
        self._author = author

        # initialize a book's owner
        self._owner = None

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else:
            raise Exception("The title must be a string!")
        
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if type(author) == str and len(author) > 4:
            self._author = author
        else:
            raise Exception("The author must be a string of greater than 4 characters!")
        
    author = property(get_author, set_author)

    # set an owner to the book
    def get_owner(self):
        return self._owner
    
    def set_owner(self, owner):
        from Owner import Owner
        if isinstance(owner, Owner):
            self._owner = owner
        else:
            raise Exception("Owner must be instance of class Owner!")
        
    owner = property(get_owner, set_owner)