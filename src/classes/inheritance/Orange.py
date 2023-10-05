# import the Cat class and inherit from it

class Orange():

    def __init__(self, color):
        # call the cat's constructor using super()
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if type(color) == str:
            self._color = color
        else:
            raise Exception
        
    # should we add new methods? override any previous ones?