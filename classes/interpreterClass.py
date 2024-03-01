
class interpreter:

    def __init__(self, dict, cmd):
        ##dictionary containing all valid words separated by type
        self.dict = dict
        self.cmd = cmd.split()

    def getAction(self, string):
        self.string = string
    
    def getObject(self, obj):
        self.obj = obj

    def getModifier(self, mod):
        self.mod = 5
    
    def getAmount(self, amt):
        self.amt = amt

    def isAction(self, string):
        ## check if string is found in action dictionary
        self.string = string
        return bool
    
    def isObject(self, obj):
        self.obj = obj
        ##check if object is found in object dictionary
        return bool
    
    def isModifier(self, mod):
        self.mod = mod
        ##check if modifier is found in modifier dictionary
        return bool
    