from orm.orm import *

class interpreter:

    
    def __init__(self, words):

        ## dictionary containing all valid words separated by type. Format:
        ##
        ## 101,attack,accurate,controlled,,
        ##     1001,rat,,6,24
        ##     1002,goblin,,8,32
        ##     1003,jad,,250,1000
        ## 102,hitpoints,,,       
        ## 103,mining,mine,
        ##     3001,tin,tinore,,,25
        ##     3002,copper,copperore,,,25
        ##     3003,iron,ironore,,,25
        ## 104,strength,aggresive,controlled
        ##     4001,rat,,6,24
        ##     4002,goblin,,8,32
        ##     4003,jad,tztok-jad,tztokjad,,250,1000
        ## 105,agility,,,
        ## 106,smithing,smelt,smith,,
        ##     6001,bronze,bronzebar,,,10
        ##     6002,iron,ironbar,,,10
        ## 107,defense,,,
        ## 108,herblore,,,
        self.words = words.split(',')
        for x, word in enumerate(self.words):
            self.words[x] = word.strip()

        #### list of skill ID and the actions associated with them
        #### i.e. 101,attack,accurate,controlled
        #### where 101 is the ID for the Attack skill and -
        #### attack, accurate, and controlled are actions that gain Attack exp

        db.connect()
        db.create_tables([Skill_pw, Action_pw, Node_pw])

        skills = []
        actions = []
        nodes = []
        test = False


        count = 0
        skCount = 0

        while(self.words[count] != "End" or test is True):
            print(self.words[count])
            skills.append(Skill_pw(name = self.words[count+1], skillID = int(self.words[count])))
            skills[skCount].save()
            count += 1
            while(self.words[count] != ""):
                actions.append(Action_pw.create(owner = skills[skCount], name = self.words[count]))
                count += 1
            count+=1
            while(self.words[count] != ""):
                for x in range (0,6):
                    print(x,'. ', self.words[count + x])
                nodes.append(Node_pw.create(owner = skills[skCount], name = self.words[count+1], nodeID = int(self.words[count]), hp = int(self.words[count + 3]), exp = int(self.words[count + 4])))
                count += 6
            if (self.words[count] == '107'):
                test = False
            else:
                count += 1
                skCount += 1
        
        db.close()





    
        

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
            x = amt
            x += 1
            self.amt = amt
        except TypeError:
            return None