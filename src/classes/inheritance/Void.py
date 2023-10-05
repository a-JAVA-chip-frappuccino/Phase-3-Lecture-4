# import the Cat class and inherit from it
from Cat import Cat

class Void(Cat):

    def __init__(self, name, age, color):
        # call the cat's constructor using super()
        super().__init__(name, age)
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
        
    # overriding method
    def meow(self):
        print("I am a black cat!")
    
    # overriding method
    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nAge: {self.age}"

cinnamon = Cat("cinnamon", 3)
nox = Void("nox", 4, "black")

nox.meow()

