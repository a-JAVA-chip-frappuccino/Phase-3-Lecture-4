class Owner():

    def __init__(self, name):
        self._name = name

        # initialize a list of books owned by self

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # add a book to the owner's list of books