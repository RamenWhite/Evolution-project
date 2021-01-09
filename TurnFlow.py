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
print('Test')