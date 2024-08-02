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
        self.invaders_killed = 0
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
            self.anvils = sorted(self.anvils, key=lambda a : a.level)
        elif oc == Models.Furance.Furance:
            self.furances.append(object)
            self.furances = sorted(self.furances, key=lambda f : f.level)
        elif oc == Models.Weapon.Weapon:
            self.weapons.append(object)
        elif oc == Models.InvaderPart.MusketeerPart:
            self.musketeerParts.append(object)
            self.musketeerParts = sorted(self.musketeerParts, key=lambda mp : mp.level)
        elif oc == Models.InvaderPart.WarriorPart:
            self.warriorParts.append(object)
            self.warriorParts = sorted(self.warriorParts, key=lambda wp : wp.level)
        elif oc == Models.Decoy.MusketeerDecoy:
            self.musketeerDecoys.append(object)
        elif oc == Models.Decoy.WarriorDecoy:
            self.warriorDecoys.append(object)
        elif oc == Models.Decoy.BattleMageDecoy:
            self.battlemageDecoys.append(object)
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
            self.cannons = sorted(self.cannons, key=lambda c : c.level)
        elif oc == Models.Resource.SteelPile:
            self.steelPile.append(object)
            self.steelPile = sorted(self.steelPile, key=lambda sp : sp.level)
        elif oc == Models.Resource.GunpowderPile:
            self.gunpowderPile.append(object)
            self.gunpowderPile = sorted(self.gunpowderPile, key=lambda gp : gp.level)
        elif oc == Models.Resource.IronCrate:
            self.ironCrates.append(object)
            self.ironCrates = sorted(self.ironCrates, key=lambda ic : ic.level)
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

    # PRIORITY
    def action_no_action(self):
        return 0

    # PRIORITY
    def action_tap_worst_anvil(self):
        if not self.anvils:
            return -1
        worst_anvil = self.anvils[0]
        anvil_product = worst_anvil.tapProduction()
        self.addToGameInventory(anvil_product)
        return 10

    # PRIORITY
    def action_tap_best_anvil(self):
        if not self.anvils:
            return -1
        best_anvil = self.anvils[-1]
        anvil_product = best_anvil.tapProduction()
        self.addToGameInventory(anvil_product)
        return 10

    def action_attack_flag_grunt(self, damage): 
        from Models.Resource import IronCrate
        if not self.flagGrunts:
            return -1
        flagGrunt = self.flagGrunts[0]
        flagGrunt.takeDamage(damage)
        if flagGrunt.getHealth() <= 0:
            self.flagGrunts.pop(0)
            self.addToGameInventory(IronCrate(1))
            return 250 + damage + flagGrunt.getHealth() * 2
        return damage

    def action_attack_spear_grunt(self, damage): 
        from Models.Resource import GunpowderPile
        if not self.spearGrunts:
            return -1
        spear_grunt = self.spearGrunts[0]
        spear_grunt.takeDamage(damage)
        if spear_grunt.getHealth() <= 0:
            self.spearGrunts.pop(0)
            self.addToGameInventory(GunpowderPile(1))
            return 500 + damage + spear_grunt.getHealth() * 2
        return damage

    def action_attack_sword_grunt(self, damage): 
        from Models.Resource import SteelPile
        if not self.swordGrunts:
            return -1
        sword_grunt = self.swordGrunts[0]
        sword_grunt.takeDamage(damage)
        if sword_grunt.getHealth() <= 0:
            self.swordGrunts.pop(0)
            self.addToGameInventory(SteelPile(1))
            return 1250 + damage + sword_grunt.getHealth() * 2
        return damage

    # PRIORITY
    def action_attack_musketeer(self, damage): 
        from Models.Resource import GunpowderPile
        if not self.musketeers:
            return -1
        musketeer = self.musketeers[0]
        musketeer.takeDamage(damage)
        if musketeer.getHealth() <= 0:
            self.musketeers.pop(0)
            self.addToGameInventory(GunpowderPile(3))
            return 15000 + damage + musketeer.getHealth() * 2
        return damage

    # PRIORITY
    def action_attack_warrior(self, damage): 
        from Models.Resource import SteelPile
        if not self.warriors:
            return -1
        warrior = self.warriors[0]
        warrior.takeDamage(damage)
        if warrior.getHealth() <= 0:
            self.warriors.pop(0)
            self.addToGameInventory(SteelPile(3))
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
    def action_merge_invader_parts(self): # TODO
        from Models.InvaderPart import MusketeerPart, WarriorPart
        if len(self.musketeerParts) > 2:
            for i in range(len(self.musketeerParts) - 1):
                f, s = self.musketeerParts[i], self.musketeerParts[i+1]
                new_musketeerParts = MusketeerPart.mergePart(f,s)
                if len(new_musketeerParts) == 1:
                    self.musketeerParts.pop(i)
                    self.musketeerParts.pop(i)
                    self.addToGameInventory(new_musketeerParts[0])
                    return new_musketeerParts[0].description
        if len(self.warriorParts) > 2:
            for i in range(len(self.warriorParts) - 1):
                f, s = self.warriorParts[i], self.warriorParts[i+1]
                new_warriorParts = WarriorPart.mergePart(f,s)
                if len(new_warriorParts) == 1:
                    self.warriorParts.pop(i)
                    self.warriorParts.pop(i)
                    self.addToGameInventory(new_warriorParts[0])
                    return new_warriorParts[0].description    
        return -1

    # PRIORITY
    def action_merge_furnace(self):
        from Models.Furance import Furance
        if len(self.furances) < 2:
            return -1
        for i in range(len(self.furances) - 1):
            f, s = self.furances[i], self.furances[i+1]
            new_furances = Furance.mergeFurance(f,s)
            if len(new_furances) == 1:
                self.furances.pop(i)
                self.furances.pop(i)
                self.addToGameInventory(new_furances[0])
                return new_furances[0].level
        return -1

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
    def action_merge_anvil(self):
        from Models.Anvil import Anvil
        if len(self.anvils) < 2:
            return -1
        for i in range(len(self.anvils) - 1):
            f, s = self.anvils[i], self.anvils[i+1]
            new_anvils = Anvil.mergeAnvil(f,s)
            if len(new_anvils) == 1:
                self.anvils.pop(i)
                self.anvils.pop(i)
                self.addToGameInventory(new_anvils[0])
                return new_anvils[0].level
        return -2

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
    def action_purchase_cannon(self): 
        from Models.Cannon import Cannon
        if self.gun_powder < 20:
            return -1
        self.updateGunpowder(-20)
        self.addToGameInventory(Cannon(1))
        remaining_damage = 100
        cost_of_gp = -100
        return remaining_damage + cost_of_gp

    def action_purchase_furnace(self): 
        from Models.Furance import Furance
        if self.gun_powder < 10 or self.steel < 5:
            return -1
        self.updateGunpowder(-10)
        self.updateSteel(-5)
        self.addToGameInventory(Furance(1))
        remaining_ore = 100
        cost_of_gp = -50
        cost_of_s = -50
        return remaining_ore + cost_of_gp + cost_of_s

    def action_purchase_anvil(self):
        from Models.Anvil import Anvil
        if self.steel < 25:
            return -1
        self.updateSteel(-25)
        self.addToGameInventory(Anvil(1))
        remaining_value = 100
        cost_of_s = -100
        return remaining_value + cost_of_s 
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

    def getResources(self):
        return self.ironCrates + self.gunpowderPile + self.steelPile
    
    def getInvaders(self):
        invaders = self.flagGrunts + self.spearGrunts + self.swordGrunts + self.musketeers + self.warriors
        invaders = sorted(invaders, key=lambda i : i.health)
        return invaders
    
    def getStructures(self):
        return self.anvils + self.furances + self.cannons
    
    def getMisc(self):
        return self.musketeerParts + self.musketeerDecoys + self.warriorParts + self.warriorDecoys + self.weapons

    def render(self):
        print("Structures\t", self.getStructures())
        print("Resources\t", self.getResources())
        print("Invaders\t", self.getInvaders())
        print("Parts & Decoys\t", self.getMisc())

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
    a1 = Models.Anvil.Anvil(4)
    a2 = Models.Anvil.Anvil(4)
    a3 = Models.Anvil.Anvil(1)
    a4 = Models.Anvil.Anvil(1)
    f1 = Models.Furance.Furance(1)
    f2 = Models.Furance.Furance(1)
    f3 = Models.Furance.Furance(1)
    f4 = Models.Furance.Furance(1)
    c1 = Models.Cannon.Cannon(1)
    c2 = Models.Cannon.Cannon(1)
    c3 = Models.Cannon.Cannon(1)
    c4 = Models.Cannon.Cannon(1)
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

    print("-------------------------------------------------------")

    g1.addToGameInventory(a1)
    g1.addToGameInventory(a2)
    g1.addToGameInventory(a3)
    g1.addToGameInventory(a4)
    # g1.addToGameInventory(a2)
    # print(g1.spearGrunts[0].health)
    # print(g1.swordGrunts[0].health)
    # print(g1.musketeers[0].health)
    # print(g1.warriors[0].health)
    g1.render()

    print("-------------------------------------------------------")

    print("Action 1\t", g1.action_merge_anvil())
    print("Action 2\t", g1.action_merge_anvil())
    print("Action 3\t", g1.action_merge_anvil())
    print("Action 4\t", g1.action_merge_anvil())
    for i in range(20):
        g1.action_tap_best_anvil()

    print("-------------------------------------------------------")

    g1.render()
    for i in range(5):
        g1.action_merge_weapons()
    while True:
        res = g1.action_merge_invader_parts()
        if res == -1:
            break

    print("-------------------------------------------------------")

    g1.render()

    print("-------------------------------------------------------")

        
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
