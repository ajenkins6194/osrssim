
class interpreter:

    
    def __init__(self, words):
        ##dictionary containing all valid words separated by type
        self.words = words.split()
        


    def splitCmd(self, cmd):
        self.cmd = cmd.split()
    



    def isAction(self, act):
        ## check if string is found in action dictionary
        self.string = act
        return bool
    
    def isObject(self, obj):
        self.obj = obj
        ##check if object is found in object dictionary
        return bool
    
    def isModifier(self, mod):
        self.mod = mod
        ##check if modifier is found in modifier dictionary
        return bool
    
    def getAction(self, act):
        if self.isAction(act):
            self.act = act
        else:
            return None

    def getModifier(self, mod):
        if self.isModifer(mod):
            self.mod = mod
        else:
            return None
    
    def getObject(self, obj):
        if self.isObject(obj):
            self.obj = obj
        else:
            return None
    
    def getAmount(self, amt):
        try:
            x += 1
            self.amt = amt
        except TypeError:
            return None