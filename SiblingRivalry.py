import Models.InvaderPart, Models.Decoy, Models.Invader
import Models.Anvil, Models.Furance, Models.Cannon
import Models.Resource, Models.Weapon

class Game:
    def __init__(self):
        self.score = 0
        self.gun_powder = 0
        self.steel = 0        
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
        self.steelPile = []
        self.ironCrates = []
    
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
            self.musketeerParts = sorted(self.musketeerParts, key=lambda mp : mp.level * -1)
        elif oc == Models.InvaderPart.WarriorPart:
            self.warriorParts.append(object)
            self.warriorParts = sorted(self.warriorParts, key=lambda mp : mp.level * -1)
        elif oc == Models.Decoy.MusketeerDecoy:
            self.musketeerDecoys.append(object)
        elif oc == Models.Decoy.WarriorDecoy:
            self.warriorDecoys.append(object)
            print("Recognized as Warrior Decoy")
        elif oc == Models.Decoy.BattleMageDecoy:
            self.battlemageDecoys.append(object)
            print("Recognized as BattleMage Decoy")
        elif oc == Models.Invader.FlagGrunt:
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
        elif oc == Models.Cannon.Cannon:
            self.cannons.append(object)
        elif oc == Models.Resource.SteelPile:
            self.steelPile.append(object)
        elif oc == Models.Resource.GunpowderPile:
            self.gunpowderPile.append(object)
        elif oc == Models.Resource.IronCrate:
            self.ironCrates.append(object)
        else:
            print("WARNING don't recognize object")
            return
        # print("Added", oc.__name__)

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
            return -1
        worst_anvil = self.anvils[0]
        anvil_product = worst_anvil.tapProduction()
        self.addToGameInventory(anvil_product)
        return 10

    def action_tap_best_anvil(self):
        if not self.anvils:
            return -1
        best_anvil = self.anvils[-1]
        anvil_product = best_anvil.tapProduction()
        self.addToGameInventory(anvil_product)
        return 10

    def action_attack_flag_grunt(self, damage):  # MOST COMPLETE
        from Models.Resource import IronCrate
        if not self.flagGrunts:
            return -1
        flagGrunt = self.flagGrunts.pop(0)
        flagGrunt.takeDamage(damage)
        if flagGrunt.getHealth() <= 0:
            self.addToGameInventory(IronCrate(1))
            return 250 + damage + flagGrunt.getHealth() * 2
        self.addToGameInventory(flagGrunt)
        return damage

    def action_attack_spear_grunt(self, damage): # TODO
        if not self.spearGrunts:
            return -1
        spear_grunt = self.spearGrunts.pop(0)
        spear_grunt.takeDamage(damage)
        if spear_grunt.getHealth() <= 0:
            return 500 + damage + spear_grunt.getHealth() * 2
        self.addToGameInventory(spear_grunt)
        return damage

    def action_attack_sword_grunt(self, damage): # TODO
        if not self.swordGrunts:
            return -1
        sword_grunt = self.swordGrunts[-1]
        sword_grunt.takeDamage(damage)
        if sword_grunt.getHealth() <= 0:
            self.swordGrunts.pop(0)
            return 1250 + damage + sword_grunt.getHealth() * 2
        return damage

    # PRIORITY
    def action_attack_musketeer(self, damage): # TODO
        if not self.musketeers:
            return -1
        musketeer = self.musketeers[-1]
        musketeer.takeDamage(damage)
        if musketeer.getHealth() <= 0:
            self.musketeer.pop(0)
            return 15000 + damage + musketeer.getHealth() * 2
        return damage

    # PRIORITY
    def action_attack_warrior(self, damage): # TODO
        if not self.warriors:
            return -1
        warrior = self.warriors[-1]
        warrior.takeDamage(damage)
        if warrior.getHealth() <= 0:
            self.warriors.pop(0)
            return 50000 + damage + warrior.getHealth() * 2
        return damage

    def action_attack_battle_mage(self, damage):
        pass

    # PRIORIY
    # Manages steel and gunpowder
    def action_merge_resources(self):
        from Models.Resource import GunpowderPile
        if len(self.gunpowderPile) < 2:
            return -1
        for i in range(len(self.gunpowderPile) - 1):
            f, s = self.gunpowderPile[i], self.gunpowderPile[i+1]
            new_gunpowderPile = GunpowderPile.mergeResource(f,s)
            if len(new_gunpowderPile) == 1:
                self.gunpowderPile.pop(i)
                self.gunpowderPile.pop(i)
                self.gunpowderPile.insert(i, new_gunpowderPile[0])
                return new_gunpowderPile[0].getResourceValue()
        return -1

    # PRIORITY
    def action_merge_invader_parts(self):
        from Models.InvaderPart import MusketeerPart
        if len(self.musketeerParts) < 2:
            return -1
        for i in range(len(self.musketeerParts) - 1):
            f, s = self.musketeerParts[i], self.musketeerParts[i+1]
            new_musketeerParts = MusketeerPart.mergePart(f,s)
            if len(new_musketeerParts) == 1:
                self.musketeerParts.pop(i)
                self.musketeerParts.pop(i)
                self.addToGameInventory(new_musketeerParts[0])
                return new_musketeerParts[0].description
        return -1

    # PRIORITY
    def action_merge_furnace(self):
        pass

    # PRIORITY
    def action_merge_weapons(self):
        from Models.Weapon import Weapon
        if len(self.weapons) < 2:
            return -1
        for i in range(len(self.weapons) - 1):
            f, s = self.weapons[i], self.weapons[i+1]
            new_weapons = Weapon.mergeWeapon(f,s)
            if len(new_weapons) == 1:
                self.weapons.pop(i)
                self.weapons.pop(i)
                self.addToGameInventory(new_weapons[0])
                return new_weapons[0].getDamage()
        return -1

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
    # Future note: should be split into however many
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

    def updateSteel(self, steel):
        self.steel = self.steel + steel
    
    def updateGunpowder(self, gun_powder):
        self.gun_powder = self.gun_powder + gun_powder

    def updateOre(self, ore):
        self.ore = self.ore + ore

    def reset(self):
        self.score = 0
        self.gun_powder = 0
        self.steel = 0        
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
        self.steelPile = []
        self.ironCrates = []

    def getOre(self) -> int:
        return self.ore
    
# TEST
    
if __name__ == "__main__":
    g1 = Game()
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
    mp1 = Models.InvaderPart.MusketeerPart(4)
    mp2 = Models.InvaderPart.MusketeerPart(4)
    wp1 = Models.InvaderPart.WarriorPart(1)
    r1 = Models.Resource.GunpowderPile(1)
    r2 = Models.Resource.GunpowderPile(1)
    r3 = Models.Resource.GunpowderPile(1)
    r4 = Models.Resource.GunpowderPile(1)
    
    # r2 = Models.Resource.SteelPile(1)
    # r3 = Models.Resource.IronCrate(1)
    w1 = Models.Weapon.Weapon(1)
    w2 = Models.Weapon.Weapon(2)

    print("---------")
    g1.addToGameInventory(a1)
    # g1.addToGameInventory(a2)
    # print(g1.spearGrunts[0].health)
    # print(g1.swordGrunts[0].health)
    # print(g1.musketeers[0].health)
    # print(g1.warriors[0].health)
    print("---------")
    for i in range(10):
        g1.action_tap_best_anvil()
    print(len(g1.weapons))
    print(g1.weapons)
    print("---------")
    count = 0
    while True:
        res = g1.action_merge_weapons()
        if res == -1:
            break
        print("Rewarded", res)
        count += 1
    print("Merged", count)
    print(g1.weapons)
    print("---------")
        
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
