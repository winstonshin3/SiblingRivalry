class Invader():
    def takeDamage(self, damage) -> int:
        self.health = self.health - damage
        return self.health

class FlagGrunt(Invader):
    def __init__(self, score, health):
        self.score = 250
        self.health = 500

class SpearGrunt(Invader):
    def __init__(self, score, health):
        self.score = 500
        self.health = 1000
    
class SwordGrunt(Invader):
    def __init__(self, score, health):
        self.score = 1250
        self.health = 2500

class Musketeer(Invader):
    def __init__(self, score, health):
        self.score = 15000
        self.health = 25000

class Warrior(Invader):
    def __init__(self):
        self.score = 50000
        self.health = 50000

class BattleMage(Invader):
    def __init__(self):
        self.score = 750000
        self.health = 500000


        
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