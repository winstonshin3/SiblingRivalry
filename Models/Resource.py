from SiblingRivalry import Game

class Resource():
    def __init__(self, name, level):
        self.name = name
        self.level = level

class IronCrate(Resource):
    def collectResource(self):
        if self.level == 1:
            Game.updateOre(2)
        elif self.level == 2:
            Game.updateIron(5)

class GunPowderPile(Resource):
    def collectResource(self):
        if self.level == 1:
            Game.updateGunPowder(2)
        elif self.level == 2:
            Game.updateGunPowder(5)
        elif self.level == 3:
            Game.updateGunPowder(12)
        elif self.level == 4:
            Game.updateGunPowder(30)

class SteelPile(Resource):
    def collectResource(self):
        if self.level == 1:
            Game.updateIron(2)
        elif self.level == 2:
            Game.updateIron(5)
        elif self.level == 3:
            Game.updateIron(12)
        elif self.level == 4:
            Game.updateIron(30)