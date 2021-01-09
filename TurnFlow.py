class TurnFlow:
    def __init__(self, guild, mob):
        self.guild = guild
        self.mob = mob
        self.index = 0
    
    def simpleCombat(self, currentMinion):

        while currentMinion.health > 0:
            allResult =  {   
                'redResult' : currentMinion.red - self.mob.red,
                'greenResult' : currentMinion.green - self.mob.green,
                'blueResult' : currentMinion.blue - self.mob.blue
            }

            outPerTurn = 0 #Dmg dealt each turn
            inPerTurn = 0 #Dmg received each turn
            for i in allResult:
                if allResult[i] <= 0:
                    inPerTurn += allResult[i]
                    currentMinion.health += inPerTurn
                    print("The minion now have ", currentMinion.health)
                    print("Damage in : " + str(allResult[i]))
                    if currentMinion.health <= 0:
                        break
                else:
                    outPerTurn += allResult[i]
                    self.mob.health -= outPerTurn
                    print("Damage out : " + str(allResult[i]))
                    
        
    def followingCombats(self):
        for i in self.guild:
            currentMinion = self.guild[self.index]
            self.simpleCombat(currentMinion)
            print ("A minion died : ", self.index)
            self.index += 1