class Game:
    score = 0
    gun_powder = 0
    iron = 0
    ore = 0
    actions_taken = 0 # Each action represents 10 seconds
    board = []

    @classmethod
    def updateScore(self, score):
        Game.score = Game.score + score

    @classmethod
    def updateIron(self, iron):
        Game.iron = Game.iron + iron
    
    @classmethod
    def updateGunPowder(self, gun_powder):
        Game.gun_powder = Game.gun_powder + gun_powder

    @classmethod
    def updateOre(self, ore):
        Game.ore = Game.ore + ore

    @classmethod
    def reset(self):
        Game.score = 0
        Game.gun_powder = 0
        Game.iron = 0        
        Game.ore = 0
        Game.actions_taken = 0
        Game.board = []





# class Cannon:



# class InvaderPart:

# class MusketeerPart(InvaderPart):

# class WarriorPart(InvaderPart):

# class AlchemyTable:

# class Upgrades:

# class Trades: