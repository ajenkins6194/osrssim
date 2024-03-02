from peewee import *

db = SqliteDatabase('skills.db')

class Skill_pw(Model):
    name = CharField()
    skillID = IntegerField()
    

    class Meta:
        database = db

class Action_pw(Model):
    owner = ForeignKeyField(Skill_pw, backref='names')
    name = CharField()

    class Meta:
        database = db

class Node_pw(Model):
    owner = ForeignKeyField(Skill_pw, backref='nodes')
    name = CharField()
    nodeID = IntegerField
    hp = IntegerField()    
    exp = IntegerField()
    

    class Meta:
        database = db

db.close()
## db.connect()
## 
## db.create_tables([Skill_pw, Action_pw, Node_pw])
## 
## ## naming convetion s_skillname s is for skill ??
## 
## s_attack = Skill_pw(name = 'Attack', skillID = 101)
## s_attack.save()
## s_mining = Skill_pw(name = 'Mining', skillID = 103)
## s_mining.save()
## 
## ## a for action 
## 
## a_attack = Action_pw.create(owner = s_attack, name = 'attack')
## a_accurate = Action_pw.create(owner = s_attack, name = 'accurate')
## a_controlled = Action_pw.create(owner = s_attack, name = 'controlled')
## a_mine = Action_pw.create(owner = s_mining, name = 'mine')
## 
## ## n for node
## 
## ## n_mob = Node_pw.create(owner = s_attack, name = 'mob', nodeID = 2001, exp = 100)
## ## n_tin = Node_pw.create(owner = s_mining, name = 'tin', nodeID = 1001, exp = 25)
## 
## action = "mine"
## node = "tin"
## 
## query = Action_pw.select(Action_pw, Skill_pw).join(Skill_pw).where(Action_pw.name == action)
## 
## for skill in query:
##     print(skill.owner.name)





