import Models.InvaderPart, Models.Decoy, Models.Invader
import Models.Anvil, Models.Furance, Models.Cannon
import Models.Resource, Models.Weapon

class Game:
    def __init__(self):
        self.score = 0
        self.gun_powder = 0
        self.iron = 0
        self.ore = 0
        self.actions_taken = 0 # Each action represents 10 seconds
        self.anvils = []
        self.furances = []
        self.weapons = []
        self.invaderParts = []
        self.decoys = []
        self.invaders = []
        self.cannons = []
        self.steelPile = []
        self.ironPile = []
        self.ironCrate = []

    def updateScore(self, score):
        self.score = self.score + score

    def updateIron(self, iron):
        self.iron = self.iron + iron
    
    def updateGunpowder(self, gun_powder):
        self.gun_powder = self.gun_powder + gun_powder

    def updateOre(self, ore):
        self.ore = self.ore + ore

    def reset(self):
        self.score = 0
        self.gun_powder = 0
        self.iron = 0        
        self.ore = 0
        self.actions_taken = 0
        self.anvils = []
        self.furances = []
        self.weapons = []
        self.musketeerParts = []
        self.warriorParts = []
        self.musketeerDecoys = []
        self.warriorDecoys = []
        self.battlemageDecoys = []
        self.invaders = []
        self.cannons = []
        self.steelPile = []
        self.ironPile = []
        self.ironCrate = []

    def getOre(self) -> int:
        return self.ore
    
    def addToGameInventory(self, object):
        oc = object.__class__
        if oc == Models.Anvil.Anvil:
            self.anvils.append(object)
            print("Recognized as Anvil")
        elif oc == Models.Furance.Furance:
            self.furances.append(object)
            print("Recognized as Furance")
        elif oc == Models.Weapon.Weapon:
            self.weapons.append(object)
            print("Recognize as Weapon")
        elif oc == Models.InvaderPart.MusketeerPart:
            self.musketeerParts(object)
            print("Recognized as Musketeer Part")
        elif oc == Models.InvaderPart.WarriorPart:
            print("Recognize as Warrior Part")
        elif oc == Models.Decoy.MusketeerDecoy:
            print("Recognized as Muskeeter Decoy")
        elif oc == Models.Decoy.WarriorDecoy:
            print("Recognized as Warrior Decoy")
        elif oc == Models.Decoy.BattleMageDecoy:
            print("Recognized as BattleMage Decoy")
        elif issubclass(oc, Models.Invader.Invader):
            self.invaders.append(object)
            print("Recognize as Invader")
        elif oc == Models.Cannon.Cannon:
            print("Recongized as Cannon")
        elif oc == Models.Resource.SteelPile:
            print("Recognize as Steel Pile")
        elif oc == Models.Resource.GunpowderPile:
            print("Recognized Gunpowder Pile")
        elif oc == Models.Resource.IronCrate:
            print("Recognize as Iron Crate")
        else:
            print("WARNING don't recognize object")
    

    
# TEST
    
if __name__ == "__main__":
    g1 = Game()
    s1 = Models.Resource.SteelPile(4)
    print(f"Before collect {g1.gun_powder}")
    g1.updateGunpowder(s1.getResourceValue())
    print(f"After collect {g1.gun_powder}")

    a1 = Models.Anvil.Anvil(1)
    c1 = Models.Cannon.Cannon(1)
    md1 = Models.Decoy.MusketeerDecoy()
    wd1 = Models.Decoy.WarriorDecoy()
    bm1 = Models.Decoy.BattleMageDecoy()
    i1 = Models.Invader.FlagGrunt()
    i2 = Models.Invader.SpearGrunt()
    i3 = Models.Invader.SwordGrunt()
    i4 = Models.Invader.Musketeer()
    i5 = Models.Invader.Warrior()
    i6 = Models.Invader.BattleMage()
    
    ip1 = Models.InvaderPart.MusketeerPart(1)
    ip2 = Models.InvaderPart.WarriorPart(1)

    r1 = Models.Resource.GunpowderPile(1)
    r2 = Models.Resource.SteelPile(1)
    r3 = Models.Resource.IronCrate(1)

    w1 = Models.Weapon.Weapon(1)
    w2 = Models.Weapon.Weapon(2)

    ap = a1.tapProduction()
    print(len(g1.anvils))
    g1.addToGameInventory(i6)
    g1.addToGameInventory(i5)
    g1.addToGameInventory(i4)
    g1.addToGameInventory(i3)
    g1.addToGameInventory(i2)
    g1.addToGameInventory(i1)
    print(len(g1.invaders))

    invader_list = g1.invaders
    print(g1.invaders)
    for invader in g1.invaders:
        print(invader.health)
    g1.invaders = sorted(g1.invaders, key=lambda invader: invader.health)
    print(g1.invaders)
        
    # s2 = a2.tapProduction()
    # print(s2.description, "\n")
    # s3 = a3.tapProduction()
    # print(s3.description, "\n")
    # s4 = a4.tapProduction()
    # print(s4.description, "\n")
    # s5 = a5.tapProduction()
    # print(s5.description, "\n")


# class Cannon:

# class AlchemyTable:

# class Upgrades:

# class Trades: