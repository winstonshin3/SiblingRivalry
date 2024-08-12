class Invader():
    def takeDamage(self, damage):
        self.health = self.health - damage
    
    def getHealth(self) -> int:
        return self.health
    
class FlagGrunt(Invader):
    def __init__(self):
        self.score = 250
        self.health = 500
    
    def __repr__(self):
        return "G1"
    
    def getScore(self) -> int:
        return self.score

class SpearGrunt(Invader):
    def __init__(self):
        self.score = 500
        self.health = 1000

    def __repr__(self):
        return "G2"
    
    def getScore(self) -> int:
        return self.score

class SwordGrunt(Invader):
    def __init__(self):
        self.score = 1250
        self.health = 2500
        
    def __repr__(self):
        return "G3"
    
    def getScore(self) -> int:
        return self.score

class Musketeer(Invader):
    def __init__(self):
        self.score = 15000
        self.health = 25000

    def getScore(self) -> int:
        return self.score

    def __repr__(self):
        return "M"

class Warrior(Invader):
    def __init__(self):
        self.score = 50000
        self.health = 50000
    
    def __repr__(self):
        return "W"

    def getScore(self) -> int:
        return self.score

class BattleMage(Invader):
    def __init__(self):
        self.score = 750000
        self.health = 500000

    def __repr__(self):
        return "BM"

    def getScore(self) -> int:
        return self.score
        
# class InvaderType(Enum):
#     FLAGGRUNT = Invader(250, 500)
#     SPEARGRUNT = Invader(500, 1000)
#     SWORDGRUNT = Invader(1250, 2500)
#     MUSKETEER = Invader(15000, 25000)
#     WARRIOR = Invader(50000, 50000)
#     BATTLEMAGE = Invader(750000,500000)

#     def __str__(self):
#         return self.name[:1]
    
# print(InvaderType.FLAGGRUNT)
# print(InvaderType.FLAGGRUNT.value)