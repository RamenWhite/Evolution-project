from random import randint

class MobBoss:
    def __init__(self):
        self.health = int
        self.red = int
        self.green = int
        self.blue = int
        self.listElement = list

    def RGB_determination(self):
        blue = randint(3, 20)
        red = randint(3, 20)
        green = randint(3, 20)
        totalPoint = blue + red + green

        supposedTotalPoint = 65
        blue = int(blue * (supposedTotalPoint / totalPoint)) #65 is the supposed total point for the boss
        red = int(red * (supposedTotalPoint / totalPoint))
        green = int(green * (supposedTotalPoint / totalPoint))

        self.listElement = [red, green, blue] #to get the position of the largest element RGB
        positionOfSmallest = self.listElement.index(min(red, green, blue))
        difference = (red + green + blue) - supposedTotalPoint 
        self.listElement[positionOfSmallest] -= difference

    def execute_creation(self):
        self.RGB_determination()
        self.health = 1000
        self.red = self.listElement[0]
        self.green = self.listElement[1]
        self.blue = self.listElement[2]

    def getHRGB(self):
        return ( 
            { 
                'health' : self.health,
                'red' : self.red,
                'green' : self.green,
                'blue' : self.blue
            }
        )
