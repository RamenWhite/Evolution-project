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
<<<<<<< HEAD

        for i in allResult:
            if allResult[i] <= 0:
                inPerTurn += allResult[i] #Addition because allresult[1] would be negative
            else:
                outPerTurn += allResult[i] 
       
        while currentMinion.health > 0:
            print("The minion has ", currentMinion.health)
            self.mob.health -= outPerTurn
            print("The mob was hit for", outPerTurn)

            currentMinion.health += inPerTurn            
            print("The minion has been hit for", abs(inPerTurn),  "\*/ He is now at", currentMinion.health)
            if currentMinion.health <= 0:
                break
                    
        
=======
        while currentMinion.health > 0:
            for i in allResult:
                if allResult[i] >= 0:
                    outPerTurn += allResult[i]
                    print("Damage out : " + str(allResult[i]))
                else:
                    inPerTurn += allResult[i]
                    print("Damage in : " + str(allResult[i]))
                    currentMinion.health += inPerTurn
                    print(currentMinion.health)
    
>>>>>>> 42236a858044eb3f61a9d756c37391e518c042d3
    def followingCombats(self):
        for i in self.guild:
            currentMinion = self.guild[self.index]
            self.simpleCombat(currentMinion)
            print("*************************************")
            print ("The minion died : ", self.index)
            print("The mob's health is now : ", self.mob.health)
            print("*************************************")
            self.index += 1