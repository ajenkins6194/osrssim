from classes.entity import entity

class node(entity):

    def __init__(self, ID, name, exp):
        entity.__init__(self, ID, name, exp)
        self.ID = ID
        self.name = name
        self.exp = exp

    def process(self):
        return self.exp
