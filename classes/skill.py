from classes.entity import entity
from classes.node import node

#skills ID numbers start with 101 for attack to 124 for total level

class skill(entity):
    
    def __init__(self, ID, name):
        entity.__init__(self, ID, name)
        self.level = 1
        self.exp = 0
    
    def setExp(self, exp):
        self.exp = exp
    
    def getExp(self):
        return self.exp
    
    def setLvl(self, lvl):
        self.level = lvl
        ##update exp value

    def getLvl(self):
        return self.level

    ##amt needs to be a number with one decimal place
    def gainExp(self, amt):
        self.exp += amt
        if self.checkLevel() is True:
            msg = ("Gained %s %s exp. Total %s exp is %s "
                   "and you reached level %s\n" % (amt, self.name, self.name, self.exp, self.level))
        else:
            msg = "Gained %s %s exp. Total %s exp is %s \n" % (amt, self.name, self.name, self.exp)
        return msg
    
    def loseExp(self, amt):
        self.exp -= amt
    
    def processCmd(self, cmd):
        msg = self.gainExp(int(cmd[1]) * int(cmd[2]))
        return msg

    def checkLevel(self):
        levels = [83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470]
        cur_level = self.level
        leveled = False
        for x in range (cur_level, 99 - cur_level):
            if levels[x - 1] < self.exp:
                self.level += 1
                leveled = True
            else:
                break

        return leveled
        



    ## for now, node is anything that gives exp
     
    def processNode(self, ID):
        nd = node(self, ID)
        self.gainExp(nd.process())


skillList = ["Attack", "Hitpoints", "Mining", "Strength", "Agility", "Smithing", "Defense", "Herblore", "Fishing", "Ranged", "Thievery", "Cooking", "Prayer", "Crafting", "Firemaking", "Magic", "Fletching", "Woodcutting", "Runecrafting", "Slayer", "Farming", "Construction", "Hunter"]
   


    
    
    
    
    