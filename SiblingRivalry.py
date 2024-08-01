import Models.InvaderPart, Models.Decoy, Models.Invader
import Models.Anvil, Models.Furance, Models.Cannon
import Models.Resource, Models.Weapon

class Game:
    def __init__(self):
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
        self.flagGrunts = []
        self.spearGrunts = []
        self.swordGrunts = []
        self.musketeers = []
        self.warriors = []
        self.battemages = []
        self.cannons = []
        self.gunpowderPile = []
        self.ironPile = []
        self.ironCrate = []
    
    def addToGameInventory(self, object):
        oc = object.__class__
        if oc == Models.Anvil.Anvil:
            self.anvils.append(object)
        elif oc == Models.Furance.Furance:
            self.furances.append(object)
        elif oc == Models.Weapon.Weapon:
            self.weapons.append(object)
        elif oc == Models.InvaderPart.MusketeerPart:
            self.musketeerParts.append(object)
        elif oc == Models.InvaderPart.WarriorPart:
            self.warriorParts.append(object)
        elif oc == Models.Decoy.MusketeerDecoy:
            self.musketeerDecoys.append(object)
            print("Recognized as Muskeeter Decoy")
        elif oc == Models.Decoy.WarriorDecoy:
            self.warriorDecoys.append(object)
            print("Recognized as Warrior Decoy")
        elif oc == Models.Decoy.BattleMageDecoy:
            self.battlemageDecoys.append(object)
            print("Recognized as BattleMage Decoy")
        elif issubclass(oc, Models.Invader.Invader):
            if oc == Models.Invader.FlagGrunt:
                self.flagGrunts.append(object)
            elif oc == Models.Invader.SpearGrunt:
                self.spearGrunts.append(object)
            elif oc == Models.Invader.SwordGrunt:
                self.swordGrunts.append(object)
            elif oc == Models.Invader.Musketeer:
                self.musketeers.append(object)
            elif oc == Models.Invader.Warrior:
                self.warriors.append(object)
            elif oc == Models.Invader.BattleMage:
                self.battemages.append(object)                
            print("Recognize as Invader")
        elif oc == Models.Cannon.Cannon:
            self.cannons.append(object)
        elif oc == Models.Resource.SteelPile:
            self.ironPile.append(object)
        elif oc == Models.Resource.GunpowderPile:
            self.gunpowderPile.append(object)
        elif oc == Models.Resource.IronCrate:
            self.ironCrate.append(object)
        else:
            print("WARNING don't recognize object")
            return
        print("Added", oc.__name__, object.level)

    # CENTRAL PERFORM ACTION FUNCTION
    def perform_action(self, action): # action is a number
        pass

    # DEFAULT GAME UPDATE
    # Returns reward value
    def action_common(self):
        pass

    # ACTION MASK
    def valid_action_mask(self):
        pass

    # ACTIONS
    # Returns reward values
    # Count: 13 - 35

    def action_no_action(self):
        return 0

    def action_tap_worst_anvil(self):
        if not self.anvils:
            return 0
        worst_anvil = self.anvils[0]
        anvil_product = worst_anvil.tapProduction()
        self.addToGameInventory(anvil_product)
        return 10

    def action_tap_best_anvil(self):
        if not self.anvils:
            return 0
        best_anvil = self.anvils[-1]
        anvil_product = best_anvil.tapProduction()
        self.addToGameInventory(anvil_product)
        return 10

    def action_attack_flag_grunt(self, damage):
        if not self.flagGrunts:
            return 0
        flag_grunt = self.flagGrunts[-1]
        hp = flag_grunt.takeDamage(damage)
        if hp <= 0:
            self.flagGrunts.pop()
            return 500
        return damage

    def action_attack_spear_grunt(self, damage):
        if not self.spearGrunts:
            return 0
        spear_grunt = self.spearGrunts[-1]
        hp = spear_grunt.takeDamage(damage)
        if hp <= 0:
            self.spearGrunts.pop()
            return 500
        return damage

    def action_attack_sword_grunt(self, damage):
        if not self.swordGrunts:
            return 0
        sword_grunts = self.swordGrunts[-1]
        hp = sword_grunts.takeDamage(damage)
        if hp <= 0:
            self.swordGrunts.pop()
            return 500
        return damage

    # PRIORITY
    def action_attack_musketeer(self, damage):
        pass

    # PRIORITY
    def action_attack_warrior(self, damage):
        pass

    def action_attack_battle_mage(self, damage):
        pass

    # PRIORIY
    # Manages iron and gunpowder
    def action_merge_resources(self):
        pass

    # PRIORITY
    def action_merge_invader_parts(self):
        pass

    # PRIORITY
    def action_merge_furnace(self):
        pass

    # PRIORITY
    def action_merge_weapons(self):
        pass

    # PRIORITY
    def action_merge_anvils(self):
        pass

    # PRIORITY
    def action_discard(self):
        pass

    def action_tap_banner(self):
        pass

    # PRIORITY
    def action_collect_resource(self): # could be split into three
        pass

    # PRIORITY: 
    # Future note: hould be split into however many
    # Purchase furances, anvils from store.
    def action_purchase_from_store(self): 
        pass

    def action_purchase_from_trade(self): # should be split
        pass

    def action_purchase_upgrade(self): # should be split
        pass

    def action_summon_decoy(self): # should be split
        pass

    # UTILITIES
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
        self.flagGrunts = []
        self.spearGrunts = []
        self.swordGrunts = []
        self.musketeers = []
        self.warriors = []
        self.battemages = []
        self.cannons = []
        self.gunpowderPile = []
        self.ironPile = []
        self.ironCrate = []

    def getOre(self) -> int:
        return self.ore
    
# TEST
    
if __name__ == "__main__":
    g1 = Game()
    s1 = Models.Resource.SteelPile(4)
    print(f"Before collect {g1.gun_powder}")
    g1.updateGunpowder(s1.getResourceValue())
    print(f"After collect {g1.gun_powder}")

    a1 = Models.Anvil.Anvil(1)
    a2 = Models.Anvil.Anvil(5)
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
    mp1 = Models.InvaderPart.MusketeerPart(1)
    wp1 = Models.InvaderPart.WarriorPart(1)
    r1 = Models.Resource.GunpowderPile(1)
    r2 = Models.Resource.SteelPile(1)
    r3 = Models.Resource.IronCrate(1)
    w1 = Models.Weapon.Weapon(1)
    w2 = Models.Weapon.Weapon(2)

    print("---------")
    g1.addToGameInventory(a1)
    g1.addToGameInventory(a2)
    for i in range(5):
        g1.action_tap_worst_anvil()
    print("---------")

    invader_list = g1.invaders
    g1.invaders = sorted(g1.invaders, key=lambda invader: invader.health)

        
    # s2 = a2.tapProduction()
    # print(s2.description, "\n")
    # s3 = a3.tapProduction()
    # print(s3.description, "\n")
    # s4 = a4.tapProduction()
    # print(s4.description, "\n")
    # s5 = a5.tapProduction()
    # print(s5.description, "\n")

# class AlchemyTable:

# class Upgrades:

# class Trades:

# class Store
