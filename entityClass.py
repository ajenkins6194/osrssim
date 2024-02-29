
class entity:

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
    def setID(self, ID):
        self.ID = ID

    def setName(self, name):
        self.name = name
    
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name