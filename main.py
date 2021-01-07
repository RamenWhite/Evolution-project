from random import randint
from Minions import Minions
from MobBoss import MobBoss
from TurnFlow import TurnFlow
from MinionsList import MinionsList

minionsList = MinionsList()
for e in range(50): #Creates 50 minion, and add it to the guild
    minionsList.create_minion()

index = 0
for j in minionsList.guild: #Show stats of all the minions
    index += 1
    print ("\nMinion #" + str(index))
    print(j.get_HRGB())

mobBoss = MobBoss()
mobBoss.execute_creation()
print('\nMobBoss stats\n', mobBoss.getHRGB())

gameMaster = TurnFlow(minionsList.guild, mobBoss) #The GameMaster is the game TurnFlower, he determines the damages
gameMaster.followingCombats()

pass
