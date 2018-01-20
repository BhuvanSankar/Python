class Fruit(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_colour(self):
        return "red"

    def __lt__(self, f):
        return self._name < f._name
    
    def __str__(self):
        return "{0} {1}".format(self.get_name(), self.get_colour())

berry = Fruit("berry")

class CitrusFruit(Fruit):
    def __init__(self, name, colour):
        super().__init__(name)
        self._colour = colour

    def get_colour(self):
        return self._colour

orange = CitrusFruit("orange", "orange")

class Lemon(CitrusFruit):
    def __init__(self, name):
        super().__init__(name, "yellow")

lemon = Lemon("lemon")

print(lemon)
