from random import randint

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

class MinionsListClass:
    def __init__ (self):
        self.guild = []
        self._index = -1
    
    def create_minion(self):
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

class TurnFlow:
    def __init__(self, guild, mob):
        self.guild = guild
        self.mob = mob
        self.index = 0
    
    def simpleCombat(self, currentMinion):
        allResult =  {   
            'redResult' : currentMinion.red - self.mob.red,
            'greenResult' : currentMinion.green - self.mob.green,
            'blueResult' : currentMinion.blue - self.mob.blue
        }

        outPerTurn = 0 #Dmg dealt each turn
        inPerTurn = 0 #Dmg received each turn
        for i in allResult:
            if allResult[i] >= 0:
                outPerTurn += allResult[i]
                print("Damage out : " + str(allResult[i]))
            else:
                inPerTurn += allResult[i]
                print("Damage in : " + str(allResult[i]))
    
    def followingCombats(self):
        for i in self.guild:
            currentMinion = self.guild[self.index]
            self.simpleCombat(currentMinion)
            self.index += 1

class MobBossClass:
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

MinionsList = MinionsListClass()
for e in range(50):
    MinionsList.create_minion()

index = 0
for j in MinionsList.guild:
    index += 1
    print ("\nMinion #" + str(index))
    print(j.get_HRGB())

MobBoss = MobBossClass()
MobBoss.execute_creation()
print('\nMobBoss stats\n', MobBoss.getHRGB())

GameMaster = TurnFlow(MinionsList.guild, MobBoss) #The GameMaster is the game TurnFlower, he determines the damages
GameMaster.followingCombats()

pass
