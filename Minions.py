class Minions:
    def __init__ (self, health, red, green, blue):
        self.health = health
        self.blue = blue
        self.red = red
        self.green = green
        self.component = [health, red, green, blue]
        self.componentName = ['health', 'red', 'green', 'blue']
        self._index = -1
    
    def get_HRGB(self):
        return (
            {
                'health' : self.health,
                'red' : self.red,
                'green' : self.green,
                'blue' : self.blue
            }
        )

    def __iter__(self):
        return self

    def __next__ (self):
        self._index += 1
        if self._index >= len(self.component):
            self._index -= 1
            raise StopIteration
        else:
            return({self.componentName[self._index] : self.component[self._index]})
