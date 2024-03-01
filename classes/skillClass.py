from classes.entityClass import entity

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
    
    def loseExp(self, amt):
        self.exp -= amt



    skillList = ["Attack", "Hitpoints", "Mining", "Strength", "Agility", "Smithing", "Defense", "Herblore", "Fishing", "Ranged", "Thievery", "Cooking", "Prayer", "Crafting", "Firemaking", "Magic", "Fletching", "Woodcutting", "Runecrafting", "Slayer", "Farming", "Construction", "Hunter"]
    


    
    
    
    
    