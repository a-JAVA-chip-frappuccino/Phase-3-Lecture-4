# import the Cat class and inherit from it
from Cat import Cat

class Orange(Cat):

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
        
    def meow(self, adjective = "fun-loving"):
        super().meow(adjective)
        print("I eat lasgana!")
        
    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nAge: {self.age}"
        
garfield = Orange("garfield", 43, "orange")
cinnamon = Cat("cinnamon", 2)

cinnamon.meow()