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
    
    def addToInventory(self, object):
        oc = object.__class__
        if oc == Models.Anvil.Anvil:
            self.anvils.append(object)
            self.anvils = sorted(self.anvils, key=lambda a : a.level)
        elif oc == Models.Furance.Furance:
            self.furances.append(object)
            self.furances = sorted(self.furances, key=lambda f : f.level)
        elif oc == Models.Weapon.Weapon:
            self.weapons.append(object)
            self.weapons = sorted(self.weapons, key=lambda f : f.level)
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
        print("Added", oc.__name__)

    # CENTRAL PERFORM ACTION FUNCTION
    def perform_action(self, action): # action is a number
        reward = -69
        if action == 1:
            reward = self.action_no_action()
        elif action == 2:
            reward = self.action_tap_worst_anvil()
        elif action == 3:
            reward = self.action_tap_best_anvil()
        elif action == 4:
            reward = self.action_attack_flag_grunt()
        elif action == 5:
            reward = self.action_attack_spear_grunt()
        elif action == 6:
            reward = self.action_attack_sword_grunt()            
        elif action == 7:
            reward = self.action_attack_musketeer()
        elif action == 8:
            reward = self.action_attack_warrior()
        elif action == 9:
            reward = self.action_merge_resources()
        elif action == 10:
            reward = self.action_merge_invader_parts()
        elif action == 11:
            reward = self.action_merge_furnace()
        elif action == 12:
            reward = self.action_merge_weapons()
        elif action == 13:
            reward = self.action_merge_anvil()
        elif action == 14:
            reward = self.action_tap_decoy()
        elif action == 15:
            reward = self.action_discard()
        elif action == 16:
            reward = self.action_collect_resource()
        elif action == 17:
            reward = self.action_purchase_cannon()
        elif action == 18:
            reward = self.action_purchase_furnace()
        elif action == 19:
            reward = self.action_purchase_anvil()
        else:
            print("Don't recognize action")
        return reward
        

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
        self.addToInventory(anvil_product)
        return 10

    # PRIORITY
    def action_tap_best_anvil(self):
        if not self.anvils:
            return -1
        best_anvil = self.anvils[-1]
        anvil_product = best_anvil.tapProduction()
        self.addToInventory(anvil_product)
        return 10

    def action_attack_flag_grunt(self, damage): 
        from Models.Resource import IronCrate
        if not self.flagGrunts:
            return -1
        flagGrunt = self.flagGrunts[0]
        flagGrunt.takeDamage(damage)
        if flagGrunt.getHealth() <= 0:
            self.flagGrunts.pop(0)
            self.addToInventory(IronCrate(1))
            self.updateKillCount()
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
            self.addToInventory(GunpowderPile(1))
            self.updateKillCount()
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
            self.addToInventory(SteelPile(1))
            self.updateKillCount()
            return 1250 + damage + sword_grunt.getHealth() * 2
        return damage

    # PRIORITY
    def action_attack_musketeer(self): 
        from Models.Resource import GunpowderPile
        if not self.musketeers:
            return -1
        if not self.weapons or self.weapons[-1].level == 0:
            return -2
        weapon = self.weapons.pop()
        damage = weapon.getDamage()
        musketeer = self.musketeers[0]
        musketeer.takeDamage(damage)
        if musketeer.getHealth() <= 0:
            self.musketeers.pop(0)
            self.addToInventory(GunpowderPile(3))
            self.updateKillCount()
            return 15000 + damage + musketeer.getHealth() * 2
        return damage

    # PRIORITY
    def action_attack_warrior(self): 
        from Models.Resource import SteelPile
        if not self.warriors:
            return -1
        if not self.weapons or self.weapons[-1].level == 0:
            return -2
        weapon = self.weapons.pop()
        damage = weapon.getDamage()
        warrior = self.warriors[0]
        warrior.takeDamage(damage)
        if warrior.getHealth() <= 0:
            self.warriors.pop(0)
            self.addToInventory(SteelPile(3))
            self.updateKillCount()
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
        if len(self.musketeerParts) > 1:
            for i in range(len(self.musketeerParts) - 1):
                f, s = self.musketeerParts[i], self.musketeerParts[i+1]
                new_musketeerParts = MusketeerPart.mergePart(f,s)
                if len(new_musketeerParts) == 1:
                    self.musketeerParts.pop(i)
                    self.musketeerParts.pop(i)
                    self.addToInventory(new_musketeerParts[0])
                    return new_musketeerParts[0].description
        print(len(self.warriorParts))
        if len(self.warriorParts) > 1:
            for i in range(len(self.warriorParts) - 1):
                f, s = self.warriorParts[i], self.warriorParts[i+1]
                new_warriorParts = WarriorPart.mergePart(f,s)
                if len(new_warriorParts) == 1:
                    self.warriorParts.pop(i)
                    self.warriorParts.pop(i)
                    self.addToInventory(new_warriorParts[0])
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
                self.addToInventory(new_furances[0])
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
                self.addToInventory(new_weapons[0])
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
                self.addToInventory(new_anvils[0])
                return new_anvils[0].level
        return -2
    
    # PRIORITY
    def action_tap_decoy(self):
        if len(self.warriorDecoys) > 0:
            warrior_decoy = self.warriorDecoys.pop(0)
            warrior = warrior_decoy.tapToSummon()
            self.addToInventory(warrior)
            return 25000
        if len(self.musketeerDecoys) > 0:
            muskeeter_decoy = self.musketeerDecoys.pop(0)
            muskeeter = muskeeter_decoy.tapToSummon()
            self.addToInventory(muskeeter)
            return 10000
        return -1

    # PRIORITY
    def action_discard(self):
        if self.weapons:
            weapon = self.weapons.pop(0)
            return weapon.getDamage() * -1
        elif self.musketeerParts:
            mp = self.musketeerParts.pop(0)
            return  mp.level * -1000
        elif self.warriorParts:
            wp = self.warriorParts.pop(0)
            return  wp.level * -2500
        elif self.warriorParts:
            wp = self.warriorParts.pop(0)
            return  wp.level * -2500
        elif self.warriorParts:
            wp = self.warriorParts.pop(0)
            return  wp.level * -2500
        elif self.cannons:
            c = self.warriorParts.pop(0)
            return  c.level * -1000
        elif self.furances:
            f = self.furances.pop(0)
            return  f.level * -10000
        elif self.anvils:
            a = self.anvils.pop(0)
            return  a.level * -100000
        else:
            return -1000000

    def action_summon_banner(self):
        pass

    def action_tap_banner(self):
        pass

    # PRIORITY
    def action_collect_resource(self): # could be split into three
        if len(self.ironCrates) > 0:
            ic = self.ironCrates.pop()
            self.updateOre(ic.getResourceValue())
            return ic.getResourceValue()
        if len(self.gunpowderPile) > 0:
            gp = self.gunpowderPile.pop()
            self.updateGunpowder(gp.getResourceValue())
            return gp.getResourceValue()
        if len(self.steelPile) > 0:
            s = self.steelPile.pop()
            self.updateSteel(s.getResourceValue())
            return s.getResourceValue()
        return -1


    # PRIORITY: 
    def action_purchase_cannon(self): 
        from Models.Cannon import Cannon
        if self.gun_powder < 20:
            return -1
        self.updateGunpowder(-20)
        self.addToInventory(Cannon(1))
        remaining_damage = 100
        cost_of_gp = -100
        return remaining_damage + cost_of_gp

    def action_purchase_furnace(self): 
        from Models.Furance import Furance
        if self.gun_powder < 10 or self.steel < 5:
            return -1
        self.updateGunpowder(-10)
        self.updateSteel(-5)
        self.addToInventory(Furance(1))
        remaining_ore = 100
        cost_of_gp = -50
        cost_of_s = -50
        return remaining_ore + cost_of_gp + cost_of_s

    def action_purchase_anvil(self):
        from Models.Anvil import Anvil
        if self.steel < 25:
            return -1
        self.updateSteel(-25)
        self.addToInventory(Anvil(1))
        remaining_value = 100
        cost_of_s = -100
        return remaining_value + cost_of_s 
        pass


    def action_purchase_from_trade(self): # should be split
        pass

    def action_purchase_upgrade(self): # should be split
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
    
    def updateKillCount(self):
        self.invaders_killed += 1

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
        print("-------------------------------------------------------")
        print("Structures\t", self.getStructures())
        print("Resources\t", self.getResources())
        print("Invaders\t", self.getInvaders())
        print("Parts & Decoys\t", self.getMisc())
        print("-------------------------------------------------------")

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
    a2 = Models.Anvil.Anvil(2)
    a3 = Models.Anvil.Anvil(3)
    a4 = Models.Anvil.Anvil(4)
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
    wp1 = Models.InvaderPart.WarriorPart(4)
    wp2 = Models.InvaderPart.WarriorPart(4)
    r1 = Models.Resource.GunpowderPile(1)
    r2 = Models.Resource.GunpowderPile(1)
    r3 = Models.Resource.GunpowderPile(1)
    r4 = Models.Resource.GunpowderPile(1)
    
    # r2 = Models.Resource.SteelPile(1)
    # r3 = Models.Resource.IronCrate(1)
    w1 = Models.Weapon.Weapon(6)
    w2 = Models.Weapon.Weapon(5)
    w3 = Models.Weapon.Weapon(5)
    w4 = Models.Weapon.Weapon(5)

    # g1.addToInventory(a2)
    # print(g1.spearGrunts[0].health)
    # print(g1.swordGrunts[0].health)
    # print(g1.musketeers[0].health)
    # print(g1.warriors[0].health)
    g1.addToInventory(a1)
    g1.addToInventory(a4)
    g1.addToInventory(wp1)
    g1.addToInventory(wp2)
    g1.addToInventory(md1)
    while True:
        g1.render()
        user_input = input("\nPerform Action: ").strip().lower()
        user_input = int(user_input)
        if user_input == -1:
            break
        print("Reward received:", g1.perform_action(user_input),"\n")


    # for i in range(5):
    #     g1.action_merge_weapons()
    # while True:
    #     res = g1.action_merge_invader_parts()
    #     if res == -1:
    #         break


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
