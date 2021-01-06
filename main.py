from random import randint

class Minions:
    def __init__ (self, health, blue, red, green):
        self.health = health
        self.blue = blue
        self.red = red
        self.green = green
        self.component = [health, blue, red, green]
        self.componentName = ['health', 'blue', 'red', 'green']
        self._index = -1
    
    def __iter__(self):
        return self

    def __next__ (self):
        self._index += 1
        if self._index >= len(self.component):
            self._index -= 1
            raise StopIteration
        else:
            return({self.componentName[self._index] : self.component[self._index]})

class MinionsListClass:
    def __init__ (self):
        self.guild = []
    
    def create_minion(self):
        health = randint(1,50)
        blue = randint(5, 50)
        red = randint(5, 50)
        green = randint(5, 50)
        minion = Minions(health, blue, red, green)
        self.guild.append(minion)

MinionsList = MinionsListClass()
MinionsList.create_minion()
listMinions = MinionsList.guild
for i in list(MinionsList.guild[0]):
    print (i)

print(MinionsList.guild[0])
pass
