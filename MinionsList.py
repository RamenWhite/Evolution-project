from random import randint
from Minions import Minions

class MinionsList:
    def __init__ (self):
        self.guild = []
        self._index = -1
    
    def create_minion(self, identity):
        self.identity = identity
        health = 20 #Every minions has the same number of HP
        blue = randint(1, 15)
        red = randint(1, 15)
        green = randint(1, 15)
        totalPoint = blue + red + green

        supposedTotalPoint = 50
        blue = int(blue * (supposedTotalPoint / totalPoint)) #50 is the supposed total point of a minion
        red = int(red * (supposedTotalPoint / totalPoint))
        green = int(green * (supposedTotalPoint / totalPoint))

        listElement = [red, green, blue] #to get the position of the largest element RGB
        positionOfSmallest = listElement.index(min(red, green, blue))
        difference = (red + green + blue) - supposedTotalPoint
        listElement[positionOfSmallest] -= difference
        minion = Minions(health, listElement[0], listElement[1], listElement[2])
        self.guild.append(minion)

    def __iter__(self):
        return(self)
    
    def __next__(self):
        self._index += 1
        if self._index >= len(self.guild):
            self._index -= 1
            raise StopIteration
        else:
            return(guild[self._index])