import Models.InvaderPart,  Models.Decoy,   Models.Invader
import Models.Anvil,        Models.Furance, Models.Cannon
import Models.Resource,     Models.Weapon

class Game:
    def __init__(self):
        self.reset()
        self.action_mapping = {
            0: self.action_no_action,
            1: self.action_tap_worst_anvil,
            2: self.action_tap_best_anvil,
            3: self.action_merge_weapons,
            4: self.action_merge_muskeeteer_parts,
            5: self.action_collect_resource,
            6: self.action_merge_gunpowder,
            7: self.action_attack_musketeer,
            8: self.action_attack_warrior,
            9: self.action_merge_anvil,
            10: self.action_merge_furnace,
            11: self.action_tap_decoy,
            12: self.action_discard,
            13: self.action_purchase_cannon,
            14: self.action_purchase_furnace,
            15: self.action_purchase_anvil,
            16: self.action_merge_steel,
            17: self.action_merge_ironcrates,
            18: self.action_merge_warrior_parts
        }

        # ACTION MASK
    def get_action_mask(self):
        mask = [True] * len(self.action_mapping)
        board_occupied = self.getBoardOccupied()
        # These policies are coupled to self.action_mapping:
        mask[0] = True
        mask[1] = bool(self.anvils) and board_occupied < 40 and self.ore >= self.anvils[0].getCost()
        mask[2] = bool(self.anvils) and board_occupied < 40 and self.ore >= self.anvils[-1].getCost()
        mask[3] = self.mergeAble(self.weapons, 5)
        mask[4] = self.mergeAble(self.musketeerParts, 4)
        mask[5] = bool(self.ironCrates or self.gunpowderPile or self.steelPile)
        mask[6] = self.mergeAble(self.gunpowderPile, 3)
        mask[7] = bool(self.musketeers) and bool(self.weapons) and self.weapons[-1].level > 0
        mask[8] = bool(self.warriors) and bool(self.weapons) and self.weapons[-1].level > 0
        mask[9] = self.mergeAble(self.anvils, 4)
        mask[10] = self.mergeAble(self.furances, 4) and board_occupied >= 40
        mask[11] = bool(self.musketeerDecoys or self.warriorDecoys)
        mask[12] = board_occupied >= 40
        mask[13] = self.gun_powder >= 20 and board_occupied < 40
        mask[14] = self.gun_powder >= 10 and self.steel >= 5 and board_occupied < 40
        mask[15] = self.steel >= 25  and board_occupied < 40
        mask[16] = self.mergeAble(self.steelPile, 3)
        mask[17] = self.mergeAble(self.ironCrates, 1)
        mask[18] = self.mergeAble(self.warriorParts, 4)

        return mask

    def reset(self):
        a1 = Models.Anvil.Anvil(1)
        m1 = Models.Invader.Musketeer()
        m2 = Models.Invader.Musketeer()
        w1 = Models.Invader.Warrior()
        f1 = Models.Furance.Furance(1)
        f2 = Models.Furance.Furance(1)
        f3 = Models.Furance.Furance(2)
        f4 = Models.Furance.Furance(2)
        f5 = Models.Furance.Furance(3)
        f6 = Models.Furance.Furance(3)

        self.score = 0
        self.actions_taken = 0
        self.invaders_killed = 0

        self.gun_powder = 25         # divide by 5
        self.steel = 15              # divide by 5
        self.ore = 50000            
        self.anvils = [a1]           
        self.furances = [f1, f2, f3, f4, f5, f6]  
        self.weapons = []           
        self.musketeerParts = []    
        self.warriorParts = []      
        self.musketeerDecoys = []   
        self.warriorDecoys = []     
        self.musketeers = [m1, m2]  
        self.warriors = [w1]        
        self.cannons = []           
        self.gunpowderPile = []     
        self.steelPile = []         
        self.ironCrates = []        

        # Currently not in use
        self.battemages = []        
        self.battlemageDecoys = []  
        self.flagGrunts = []        
        self.spearGrunts = []       
        self.swordGrunts = []       

    def addToInventory(self, obj):
        oc = obj.__class__
        self.inventory_map = {
            Models.Anvil.Anvil: (self.anvils, 'level'),
            Models.Furance.Furance: (self.furances, 'level'),
            Models.Weapon.Weapon: (self.weapons, 'level'),
            Models.InvaderPart.MusketeerPart: (self.musketeerParts, 'level'),
            Models.InvaderPart.WarriorPart: (self.warriorParts, 'level'),
            Models.Decoy.MusketeerDecoy: (self.musketeerDecoys, None),
            Models.Decoy.WarriorDecoy: (self.warriorDecoys, None),
            Models.Decoy.BattleMageDecoy: (self.battlemageDecoys, None),
            Models.Invader.FlagGrunt: (self.flagGrunts, None),
            Models.Invader.SpearGrunt: (self.spearGrunts, None),
            Models.Invader.SwordGrunt: (self.swordGrunts, None),
            Models.Invader.Musketeer: (self.musketeers, None),
            Models.Invader.Warrior: (self.warriors, None),
            Models.Invader.BattleMage: (self.battemages, None),
            Models.Cannon.Cannon: (self.cannons, 'level'),
            Models.Resource.SteelPile: (self.steelPile, 'level'),
            Models.Resource.GunpowderPile: (self.gunpowderPile, 'level'),
            Models.Resource.IronCrate: (self.ironCrates, 'level')
        }
        if oc in self.inventory_map:
            inventory_list, sort_key = self.inventory_map[oc]
            inventory_list.append(obj)
            if sort_key:
                inventory_list.sort(key=lambda x: getattr(x, sort_key)) #getattr error is not handled
        else:
            print("WARNING: don't recognize object")


    def mergeAble(self, object_list, limit):
        if len(object_list) < 2:
            return False
        for i in range(len(object_list) - 1):
            if object_list[i].level == object_list[i+1].level and object_list[i].level <= limit:
                return True
        return False
    
    def perform_action(self, action): # action is a number
        mask = self.get_action_mask()
        if action > len(mask) - 1 or action < 0:
            return -10000
        if not mask[action]:
            return -1000
        action_function = self.action_mapping.get(action)
        if action_function:
            reward = action_function()
        else:
            print("Don't recognize action")
        stateOreProduced = self.getOreProduction()
        stateDamageProduced = self.getDamageProduction()
        self.updateOre(stateOreProduced)
        self.actions_taken += 1
        return reward
    
    # DEFAULT GAME UPDATE
    # Returns reward value
    def updateCannonDamage(self, invaders, damage):
        for i in invaders:
            i.takeDamage(damage)
    

    def getOreProduction(self):
        total_production = 0
        for f in self.furances:
            total_production += f.produceOre()
        return total_production
    
    def getDamageProduction(self):
        total_production = 0
        for c in self.cannons:
            total_production += c.getDamage()
        return total_production

    # RETURN OBSERVATION
    def getObservation(self):
        obs = [
            self.gun_powder // 5,
            self.steel // 5,
            len(self.furances),
            int(self.getOreProduction() * 0.36),
            len(self.cannons),
            int(self.getDamageProduction() * 0.02),
            len(self.anvils),
            len(self.weapons),
            len(self.musketeerParts),
            len(self.warriorParts),
            len(self.musketeerDecoys),
            len(self.warriorDecoys),
            len(self.musketeers),
            len(self.warriors),
            len(self.gunpowderPile),
            len(self.steelPile),
            len(self.ironCrates)
        ]
        return obs


    # ACTIONS
    def action_no_action(self):
        return 0

    def action_tap_worst_anvil(self):
        anvil = self.anvils[0]
        return self.helper_tap_anvil(anvil)
        
    def action_tap_best_anvil(self):
        anvil = self.anvils[-1]
        return self.helper_tap_anvil(anvil)
    
    def helper_tap_anvil(self, anvil):
        cost = anvil.getCost()
        anvil_product = anvil.tapProduction()
        self.addToInventory(anvil_product)
        self.updateOre(cost * -1)
        return 1

    def action_attack_flag_grunt(self): 
        from Models.Resource import IronCrate
        return self.helper_attack_invader(self.flagGrunts, IronCrate(1))

    def action_attack_spear_grunt(self):
        from Models.Resource import GunpowderPile
        return self.helper_attack_invader(self.spearGrunts, GunpowderPile(1))

    def action_attack_sword_grunt(self): 
        from Models.Resource import SteelPile
        return self.helper_attack_invader(self.swordGrunts, SteelPile(1))

    def action_attack_musketeer(self): 
        from Models.Resource import GunpowderPile
        return self.helper_attack_invader(self.musketeers, GunpowderPile(3))
    
    def action_attack_warrior(self): 
        from Models.Resource import SteelPile
        return self.helper_attack_invader(self.warriors, SteelPile(3))
    
    def action_attack_battle_mage(self):
        pass
    
    def helper_attack_invader(self, invaders, reward):
        weapon = self.weapons.pop()
        damage = weapon.getDamage()
        invader = invaders[0]
        invader.takeDamage(damage)
        if invader.getHealth() <= 0:
            invaders.pop(0)
            self.addToInventory(reward)
            self.updateKillCount()
            self.updateScore(invader.score)
            return invader.score
        return 0

    def action_merge_ironcrates(self):
        return self.helper_merge(self.ironCrates, 2)
    
    def action_merge_gunpowder(self):
        return self.helper_merge(self.gunpowderPile, 4)
    
    def action_merge_steel(self):
        return self.helper_merge(self.steelPile, 4)

    def action_merge_weapons(self):
        return self.helper_merge(self.weapons, 6)

    def action_merge_muskeeteer_parts(self):
        return self.helper_merge(self.musketeerParts, 5) # Specially 5 refactor?
    
    def action_merge_warrior_parts(self):
        return self.helper_merge(self.warriorParts, 5) # Specially 5 refactor?

    def action_merge_furnace(self):
        return self.helper_merge(self.furances, 5)

    def action_merge_anvil(self):
        return self.helper_merge(self.anvils, 5)
    
    def helper_merge(self, mergables, levelLimit):
        for i in range(len(mergables) - 1):
            x, y = mergables[i], mergables[i+1]
            if x.getLevel() == y.getLevel() and x.getLevel() < levelLimit:
                mergables.pop(i)
                mergables.pop(i)
                z = x.getUpgrade()
                self.addToInventory(z)
                return 1
        return -1
    
    # PRIORITY
    def action_tap_decoy(self):
        if len(self.warriorDecoys) > 0:
            warrior_decoy = self.warriorDecoys.pop(0)
            warrior = warrior_decoy.tapToSummon()
            self.addToInventory(warrior)
            return 1
        if len(self.musketeerDecoys) > 0:
            muskeeter_decoy = self.musketeerDecoys.pop(0)
            muskeeter = muskeeter_decoy.tapToSummon()
            self.addToInventory(muskeeter)
            return 1
        return -1

    # PRIORITY
    def action_discard(self):
        if self.weapons:
            weapon = self.weapons.pop(0)
        elif self.musketeerParts:
            mp = self.musketeerParts.pop(0)
        elif self.warriorParts:
            wp = self.warriorParts.pop(0)
        elif self.cannons:
            c = self.cannons.pop(0)
        elif self.furances:
            f = self.furances.pop(0)
        elif self.anvils:
            a = self.anvils.pop(0)
        return -1

    def action_summon_banner(self):
        pass

    def action_tap_banner(self):
        pass

    # PRIORITY
    def action_collect_resource(self): # could be split into three
        if len(self.ironCrates) > 0:
            ic = self.ironCrates.pop()
            self.updateOre(ic.getResourceValue())
            return 1
        if len(self.gunpowderPile) > 0:
            gp = self.gunpowderPile.pop()
            self.updateGunpowder(gp.getResourceValue())
            return 1
        if len(self.steelPile) > 0:
            s = self.steelPile.pop()
            self.updateSteel(s.getResourceValue())
            return 1
        return -1


    # PRIORITY: 
    def action_purchase_cannon(self): 
        from Models.Cannon import Cannon
        self.updateGunpowder(-20)
        self.addToInventory(Cannon(1))
        return -1

    def action_purchase_furnace(self): 
        from Models.Furance import Furance
        self.updateGunpowder(-10)
        self.updateSteel(-5)
        self.addToInventory(Furance(1))
        return -1

    def action_purchase_anvil(self):
        from Models.Anvil import Anvil
        self.updateSteel(-25)
        self.addToInventory(Anvil(1))
        return -1

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
        invaders = (self.flagGrunts + 
                    self.spearGrunts + 
                    self.swordGrunts + 
                    self.musketeers + 
                    self.warriors)
        invaders = sorted(invaders, key=lambda i : i.health)
        return invaders
    
    def getStructures(self):
        return self.anvils + self.furances + self.cannons
    
    def getMisc(self):
        return (self.musketeerParts + 
                self.musketeerDecoys + 
                self.warriorParts + 
                self.warriorDecoys)

    def getBoardOccupied(self):
        return (len(self.anvils) +
                len(self.furances) + 
                len(self.weapons) + 
                len(self.musketeerParts) + 
                len(self.warriorParts) + 
                len(self.musketeerDecoys) + 
                len(self.warriorDecoys) + 
                len(self.musketeers) + 
                len(self.warriors) + 
                len(self.cannons) + 
                len(self.gunpowderPile) + 
                len(self.steelPile) + 
                len(self.ironCrates))

    def render(self):
        print("---------------------------------------------------------------------------------")
        print(f"Score\t\t\t{self.score}\tStructures\t", self.getStructures())
        print(f"Ore\t\t\t{self.ore}\tResources\t", self.getResources())
        print(f"Gunpowder\t\t{self.gun_powder}\tInvaders\t", self.getInvaders())
        print(f"Steel\t\t\t{self.steel}\tParts & Decoys\t", self.getMisc())
        print(f"Invaders Killed\t\t{self.invaders_killed}\tWeapons\t\t", self.weapons)
        print(f"Action Taken\t\t{self.actions_taken}\tBoard Occupied\t", self.getBoardOccupied())
        print("---------------------------------------------------------------------------------")

    def getOre(self) -> int:
        return self.ore
    
# TEST
    
if __name__ == "__main__":
    g1 = Game()
    while True:
        g1.render()
        print("Action mask:", g1.get_action_mask())
        print("Observation:", g1.getObservation())
        user_input = input("\nPerform Action: ").strip().lower()
        try:
            user_input = int(user_input)
            if user_input == -1:
                break
            print("Reward received:", g1.perform_action(user_input),"\n")
        except:
            print("Action not recognized")