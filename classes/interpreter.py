from orm.orm import *

class interpreter:

    
    def __init__(self, words):

        ## dictionary containing all valid words separated by type. Format: OUTDATED
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

        while(self.words[count] != "End"):
            skills.append(Skill_pw(name = self.words[count+1], skillID = int(self.words[count])))
            skills[skCount].save()
            count += 1
            while(self.words[count] != ""):
                actions.append(Action_pw.create(owner = skills[skCount], name = self.words[count]))
                count += 1
            count+=1
            while (self.words[count] != ""):
                long_name = ""
                id = self.words[count]
                count += 1
                temp_name = self.words[count]
                while(self.words[count] != ""):
                    ## need to figure out how to have items have multiple names point to the same item
                    ## remove temp_name
                    ## long_name += self.words[count] + ','
                    count += 1
                nodes.append(Node_pw.create(owner = skills[skCount], name = temp_name, nodeID = int(id), hp = 0, exp = 0, level_req = 0))    
                count += 1
                nodes[len(nodes) - 1].hp = int(self.words[count])
                nodes[len(nodes) - 1].save()
                count += 1
                nodes[len(nodes) - 1].exp = int(self.words[count])
                nodes[len(nodes) - 1].save()
                count += 1
                nodes[len(nodes) - 1].level_req = int(self.words[count])
                nodes[len(nodes) - 1].save()
                count += 2
            count += 1
            skCount += 1
        
        db.close()
       

    def interpret(self, cmd, req):
        self.cmd = cmd.split()

        ## [0] = skill ID, [1] = exp to add
        interpreted_Cmd = []

        for x, c in enumerate(self.cmd):
            self.cmd[x] = c.strip()
        
        db.connect()
        
        skill = (Action_pw
                 .select(Action_pw, Skill_pw)
                 .join(Skill_pw)
                 .where(Action_pw.name == self.cmd[0]))
        
        ## we know the skill. figure out how to only search through that skill
        node = (Node_pw
                .select(Node_pw, Skill_pw)
                .join(Skill_pw)
                .where(Node_pw.name == self.cmd[1]))
        
        match = 0
        

        for x in range (0, len(node)):
            if node[x].owner.skillID == skill[0].owner.skillID:
                match = x
        
        interpreted_Cmd.append(skill[0].owner.skillID - 101)
        interpreted_Cmd.append(node[0].exp)
        try:
            interpreted_Cmd.append(self.cmd[2])
        except:
            interpreted_Cmd.append(1)
        if req == 1:
            interpreted_Cmd.append(node[match].level_req)
        else:
            interpreted_Cmd.append(1)
        

        db.close()

        return interpreted_Cmd


        

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