from entityClass import entity

class monster(entity):

    def __init__(self, ID, name, level, hp):
        entity.__init__(self, ID, name)
        self.hp = hp
        self.level = level