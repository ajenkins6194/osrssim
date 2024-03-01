
class interpreter:

    
    def __init__(self, words):

        ## dictionary containing all valid words separated by type. Format:
        ##
        ## Actions:
        ##   101,attack,accurate,controlled
        ##   102,
        ##   103,mine
        ##   104,strength,aggresive,controlled
        ## Objects:
        ##    1001,tin,tinore
        ## Modifiers:
        ##    until
        ## End

        self.words = words.split()

        ## list of skill ID and the actions associated with them
        ## i.e. 101,attack,accurate,controlled
        ## where 101 is the ID for the Attack skill and -
        ## attack, accurate, and controlled are actions that gain Attack exp
    
        self.actions = []

        ## list of object ID and the names associated with them
        ## i.e. 1001,tin,tinore
        ## where 1001 is the ID for Tin Ore

        self.objects = []

        ## list of valid modifiers

        self.modifiers = []

        count = 0

        while self.words[count] != "Objects:":
            self.actions.append(self.words[count])
            count+=1

        while self.words[count] != "Modifiers:":
            self.objects.append(self.words[count])
            count +=1

        while self.words[count] != "End":
            self.modifiers.append(self.words[count])
            count+=1


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