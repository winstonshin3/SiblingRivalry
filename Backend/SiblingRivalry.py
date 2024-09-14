import Models.Alchemy
import Models.Banner
import Models.InvaderPart,  Models.Decoy,   Models.Invader
import Models.Anvil,        Models.Furance, Models.Cannon
import Models.Resource,     Models.Weapon
import ActionStrategy

class Game:

    MAX_BOARD_SPACE = 38
    SECONDS_PER_ACTION = 10

    def __init__(self):
        self.reset()
    
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

        self.day = 1 
        self.score = 0
        self.actions_taken = 0
        self.invaders_killed = 0
        self.banner_holder = Models.Banner.BannerHolder()
        self.gun_powder = 25         # divide by 5
        self.steel = 15             # divide by 5
        self.ore = 50000
        self.ore_cap = 100000           
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
        self.banners = []   
        self.flagGrunts = []        
        self.spearGrunts = []       
        self.swordGrunts = []
        self.battlemages = []        
        self.battlemageDecoys = []
        self.alchemyTables = []
        self.bombs = []

        # For Upgrades
        self.score_multiplier = 1
        self.score_multiplier_level = 0

        self.banner_time_reduction = 1
        self.banner_time_reduction_level = 0

        self.iron_cap_multiplier = 1
        self.iron_cap_multiplier_level = 0

        self.weapon_damage_multiplier = 1
        self.weapon_damage_multiplier_level = 0

        self.cannon_damage_multiplier = 1
        self.cannon_damage_multiplier_level = 0

        self.bomb_damage_multiplier = 1
        self.bomb_damage_multiplier_level = 0

        # For Trades
        self.trade_1 = True
        self.trade_2 = True
        self.trade_3 = True
        self.trade_4 = True

        # For statistics
        self.gp_collected = 0
        self.s_collected = 0
        self.discard = 0

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
            18: self.action_merge_warrior_parts,
            19: self.action_summon_banner,
            20: self.action_tap_banner,
            21: self.action_attack_flag_grunt,
            22: self.action_attack_spear_grunt,
            23: self.action_attack_sword_grunt,
            24: self.action_merge_cannon,
            25: self.action_purchase_alchemy_table,
            26: self.action_tap_alchemy_table,
            27: self.action_merge_bomb,
            28: self.action_merge_alchemy_table,
            29: self.action_attack_battlemage,
            30: self.action_use_bomb,
            31: self.action_purchase_battle_mage_decoy,
            32: self.action_upgrade_1,
            33: self.action_upgrade_2,
            34: self.action_upgrade_3,
            35: self.action_upgrade_4,
            36: self.action_upgrade_5,
            37: self.action_upgrade_6,
            38: self.action_purchase_trade_1,
            39: self.action_purchase_trade_2,
            40: self.action_purchase_trade_3,
            41: self.action_purchase_trade_4
        }

    def get_action_mask(self):
        mask = [True] * len(self.action_mapping)
        board_occupied = self.getBoardOccupied()
        board_available = board_occupied < Game.MAX_BOARD_SPACE
        banner_stock = self.banner_holder.getStock()
        weapons_available = bool(self.weapons) and self.weapons[-1].level > 0
        bombs_available = bool(self.bombs) and self.bombs[-1].level > 2
        # These policies are coupled to self.action_mapping:
        mask[0] = True
        mask[1] = bool(self.anvils) and board_available and self.ore >= self.anvils[0].getCost()
        mask[2] = bool(self.anvils) and board_available and self.ore >= self.anvils[-1].getCost()
        mask[3] = self.mergeAble(self.weapons, 5)
        mask[4] = self.mergeAble(self.musketeerParts, 4)
        mask[5] = bool(self.ironCrates or self.gunpowderPile or self.steelPile)
        mask[6] = self.mergeAble(self.gunpowderPile, 3)
        mask[7] = bool(self.musketeers) and weapons_available
        mask[8] = bool(self.warriors) and weapons_available
        mask[9] = self.mergeAble(self.anvils, 4)
        mask[10] = self.mergeAble(self.furances, 4) and board_occupied >= Game.MAX_BOARD_SPACE
        mask[11] = bool(self.musketeerDecoys or self.warriorDecoys or self.battlemageDecoys)
        mask[12] = board_occupied >= Game.MAX_BOARD_SPACE
        mask[13] = self.gun_powder >= 20 and board_available and self.invaders_killed >= 10
        mask[14] = self.gun_powder >= 10 and self.steel >= 5 and board_available and self.invaders_killed >= 25
        mask[15] = self.steel >= 25  and board_available and self.invaders_killed >= 50
        mask[16] = self.mergeAble(self.steelPile, 3)
        mask[17] = self.mergeAble(self.ironCrates, 1)
        mask[18] = self.mergeAble(self.warriorParts, 4)
        mask[19] = banner_stock > 0 and banner_stock <= 10 and board_available
        mask[20] = bool(self.banners) and   board_available
        mask[21] = bool(self.flagGrunts) and weapons_available
        mask[22] = bool(self.spearGrunts) and weapons_available
        mask[23] = bool(self.swordGrunts) and weapons_available
        mask[24] = self.mergeAble(self.cannons, 4) and board_occupied >= Game.MAX_BOARD_SPACE
        mask[25] = self.steel >= 20 and self.gun_powder >= 40 and board_available and self.invaders_killed >= 200
        mask[26] = bool(self.alchemyTables)
        mask[27] = self.mergeAble(self.bombs, 3)
        mask[28] = self.mergeAble(self.alchemyTables, 2)
        mask[29] = bool(self.battlemages) and weapons_available
        mask[30] = bool(self.battlemages) and bombs_available
        mask[31] = self.steel >= 40 and board_available and self.invaders_killed >= 100
        mask[32] = self.mask_upgrade_1() 
        mask[33] = self.mask_upgrade_2()
        mask[34] = self.mask_upgrade_3()
        mask[35] = self.mask_upgrade_4()
        mask[36] = self.mask_upgrade_5()
        mask[37] = self.mask_upgrade_6() and bool(self.alchemyTables)
        mask[38] = self.mask_trade_1() and board_available
        mask[39] = self.mask_trade_2() and board_available
        mask[40] = self.mask_trade_3() and board_available
        mask[41] = self.mask_trade_4() and board_available
        return mask

        
    # TO TEST
    def addToInventory(self, obj):
        oc = obj.__class__
        inventory_map = {
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
            Models.Invader.BattleMage: (self.battlemages, None),
            Models.Cannon.Cannon: (self.cannons, 'level'),
            Models.Resource.SteelPile: (self.steelPile, 'level'),
            Models.Resource.GunpowderPile: (self.gunpowderPile, 'level'),
            Models.Resource.IronCrate: (self.ironCrates, 'level'),
            Models.Banner.Banner: (self.banners, 'level'),
            Models.Alchemy.AlchemyTable: (self.alchemyTables, 'level'),
            Models.Alchemy.Bomb: (self.bombs, 'level')
        }
        if oc in inventory_map:
            inventory_list, sort_key = inventory_map[oc]
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
            len(self.battlemageDecoys),
            len(self.flagGrunts),
            len(self.spearGrunts),
            len(self.swordGrunts),
            len(self.musketeers),
            len(self.warriors),
            len(self.battlemages),
            len(self.gunpowderPile),
            len(self.steelPile),
            len(self.ironCrates),
            self.banner_holder.getStock(),
            len(self.banners),
            len(self.bombs),
            len(self.alchemyTables),
            self.score_multiplier_level,
            self.banner_time_reduction_level,
            self.iron_cap_multiplier_level,
            self.weapon_damage_multiplier_level,
            self.cannon_damage_multiplier_level,
            self.bomb_damage_multiplier_level
        ]
        return obs
    
    def perform_action(self, action): # action is a number        
        action_function = self.action_mapping.get(action)
        if action_function:
            reward = action_function()
        else:
            print("Don't recognize action")

        stateOreProduced = self.getOreProduction()
        reward_from_cannons = self.updateCannonDamage()
        self.updateOre(stateOreProduced)
        self.updateActionsTaken()

        if self.actions_taken % int(86400 / Game.SECONDS_PER_ACTION) == 0:
            self.updateDay()

        if self.actions_taken % int((5400 - self.banner_time_reduction) / Game.SECONDS_PER_ACTION) == 0 and self.banner_holder.getStock() < 10:
            self.banner_holder.restock()

        return reward + reward_from_cannons
    
    # DEFAULT GAME UPDATE
    def updateCannonDamage(self):
        damage = self.getDamageProduction()
        invaders = self.getInvaders()
        reward = 0
        for invader in invaders:
            invader.takeDamage(damage)
            if invader.getHealth() > 0:
                break
            self.updateKillCount()
            self.updateScore(invader.getScore())
            damage = invader.getHealth() * -1
            reward += invader.getScore()
        self.flagGrunts = []
        self.spearGrunts = []
        self.swordGrunts = []
        self.musketeers = []
        self.warriors = []
        self.battlemages = []
        for invader in invaders:
            invader_class = invader.__class__
            if invader.getHealth() > 0:
                self.addToInventory(invader)
            else:
                if invader_class == Models.Invader.FlagGrunt:
                    self.addToInventory(Models.Resource.IronCrate(1))
                elif invader_class == Models.Invader.SpearGrunt:
                    self.addToInventory(Models.Resource.GunpowderPile(1))
                elif invader_class == Models.Invader.SwordGrunt:
                    self.addToInventory(Models.Resource.SteelPile(1))
                elif invader_class == Models.Invader.Musketeer:
                    self.addToInventory(Models.Resource.GunpowderPile(3))
                elif invader_class == Models.Invader.Warrior:
                    self.addToInventory(Models.Resource.GunpowderPile(3))
        return reward

    def getOreProduction(self):
        total_production = 0
        for f in self.furances:
            total_production += f.produceOre()
        return int(total_production * Game.SECONDS_PER_ACTION / 10)
    
    def getDamageProduction(self):
        total_production = 0
        for c in self.cannons:
            total_production += c.getDamage()
        return int(total_production * self.cannon_damage_multiplier * Game.SECONDS_PER_ACTION / 180)


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
    
    def action_tap_alchemy_table(self):
        alchemy_table = self.alchemyTables[-1]
        cost = alchemy_table.getCost()
        table_product = alchemy_table.tapProduction()
        self.addToInventory(table_product)
        self.updateGunpowder(cost * -1)
        return 0
    
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

    def helper_attack_invader(self, invaders, reward):
        weapon = self.weapons.pop()
        damage = weapon.getDamage() * self.weapon_damage_multiplier
        invader = invaders[0]
        invader.takeDamage(damage)
        if invader.getHealth() <= 0:
            invaders.pop(0)
            self.addToInventory(reward)
            self.updateKillCount()
            self.updateScore(invader.score)
            return int(invader.score / 100)
        return 0

    def action_merge_ironcrates(self):
        return self.helper_merge(self.ironCrates, 2, 1)
    
    def action_merge_gunpowder(self):
        return self.helper_merge(self.gunpowderPile, 4, 1)
    
    def action_merge_steel(self):
        return self.helper_merge(self.steelPile, 4, 1)

    def action_merge_weapons(self):
        return self.helper_merge(self.weapons, 6, 1)

    def action_merge_muskeeteer_parts(self):
        return self.helper_merge(self.musketeerParts, 5, 1) # Specially 5 refactor?
    
    def action_merge_warrior_parts(self):
        return self.helper_merge(self.warriorParts, 5, 1) # Specially 5 refactor?

    def action_merge_furnace(self):
        return self.helper_merge(self.furances, 5, -1)

    def action_merge_anvil(self):
        return self.helper_merge(self.anvils, 5, 0)
    
    def action_merge_cannon(self):
        return self.helper_merge(self.cannons, 5, -1)
    
    def action_merge_alchemy_table(self):
        return self.helper_merge(self.alchemyTables, 3, -1)
    
    def action_merge_bomb(self):
        return self.helper_merge(self.bombs, 4, -1)
    
    def helper_merge(self, mergables, levelLimit, reward):
        for i in range(len(mergables) - 1):
            x, y = mergables[i], mergables[i+1]
            if x.getLevel() == y.getLevel() and x.getLevel() < levelLimit:
                mergables.pop(i)
                mergables.pop(i)
                z = x.getUpgrade()
                self.addToInventory(z)
                return reward
        return -1
    
    def action_tap_decoy(self):
        if len(self.warriorDecoys) > 0:
            warrior_decoy = self.warriorDecoys.pop(0)
            warrior = warrior_decoy.tapToSummon()
            self.addToInventory(warrior)
            return 0
        if len(self.battlemageDecoys) > 0:
            battlemage_decoy = self.battlemageDecoys.pop(0)
            battlemage = battlemage_decoy.tapToSummon()
            self.addToInventory(battlemage)
            return 0
        if len(self.musketeerDecoys) > 0:
            muskeeter_decoy = self.musketeerDecoys.pop(0)
            muskeeter = muskeeter_decoy.tapToSummon()
            self.addToInventory(muskeeter)
            return 0
        return -1
    
    def action_discard(self):
        if self.weapons:
            self.weapons.pop(0)
        elif self.musketeerParts:
            self.musketeerParts.pop(0)
        elif self.warriorParts:
            self.warriorParts.pop(0)
        elif self.bombs:
            self.bombs.pop(0)
        elif self.cannons:
            self.cannons.pop(0)
        elif self.furances:
            self.furances.pop(0)
        elif self.anvils:
            self.anvils.pop(0)
        self.discard += 1
        return -10

    def action_collect_resource(self): # could be split into three
        if len(self.ironCrates) > 0:
            ic = self.ironCrates.pop()
            self.updateOre(ic.getResourceValue() * self.iron_cap_multiplier)
            return ic.getLevel()
        if len(self.gunpowderPile) > 0:
            gp = self.gunpowderPile.pop()
            self.updateGunpowder(gp.getResourceValue())
            self.gp_collected += gp.getResourceValue()
            return gp.getLevel()
        if len(self.steelPile) > 0:
            s = self.steelPile.pop()
            self.updateSteel(s.getResourceValue())
            self.s_collected += s.getResourceValue()
            return s.getLevel()
        return -1
        
    def action_purchase_cannon(self): 
        from Models.Cannon import Cannon
        self.updateGunpowder(-20)
        self.addToInventory(Cannon(1))
        return 1

    def action_purchase_furnace(self): 
        from Models.Furance import Furance
        self.updateGunpowder(-10)
        self.updateSteel(-5)
        self.addToInventory(Furance(1))
        return 0

    def action_purchase_anvil(self):
        from Models.Anvil import Anvil
        self.updateSteel(-25)
        self.addToInventory(Anvil(1))
        return 0
    
    def action_purchase_alchemy_table(self): # should be split
        from Models.Alchemy import AlchemyTable
        self.alchemyTables.append(AlchemyTable(1))
        self.updateGunpowder(-40)
        self.updateSteel(-20)
        return 0
    
    def action_summon_banner(self):
        banner = self.banner_holder.tap()
        self.addToInventory(banner)
        return -1
    
    def action_tap_banner(self):
        self.banners = sorted(self.banners, key=lambda banner : banner.level)
        banner = self.banners[0]
        invader = banner.tap()
        self.addToInventory(invader)
        if banner.getLevel() > 2:
            self.banners.pop(0)
        return 0
    
    # TO TEST
    def action_attack_battlemage(self):
        weapon = self.weapons.pop()
        damage = weapon.getDamage() * self.weapon_damage_multiplier
        invader = self.battlemages[0]
        invader.takeDamage(damage)
        if invader.getHealth() <= 0:
            self.battlemages.pop(0)
            self.updateKillCount()
            self.updateScore(invader.score)
            return int(invader.score / 100)
        return 0

    def action_use_bomb(self):
        bomb = self.bombs.pop()
        damage = bomb.getDamage() * self.bomb_damage_multiplier
        invader = self.battlemages[0]
        invader.takeDamage(damage)
        if invader.getHealth() <= 0:
            self.battlemages.pop(0)
            self.updateKillCount()
            self.updateScore(invader.score)
            return int(invader.score / 100)
        return 0

    def action_purchase_battle_mage_decoy(self):
        from Models.Decoy import BattleMageDecoy
        self.updateSteel(-40)
        self.addToInventory(BattleMageDecoy())
        return 0

    def action_upgrade_1(self):
        self.score_multiplier_level += 1
        if self.score_multiplier_level == 1:
            self.score_multiplier = 1.1
            self.updateSteel(-10)
        elif self.score_multiplier_level == 2:
            self.score_multiplier = 1.2
            self.updateSteel(-15)
            self.updateGunpowder(-25)
        elif self.score_multiplier_level == 3:
            self.score_multiplier = 1.3
            self.updateGunpowder(-50)
        elif self.score_multiplier_level == 4:
            self.score_multiplier = 1.4
            self.updateSteel(-25)
            self.updateGunpowder(-50)    
        elif self.score_multiplier_level == 5:
            self.score_multiplier = 1.5
            self.updateSteel(-75)
        return 0

    def mask_upgrade_1(self):
        if self.score_multiplier_level == 0:
            return self.steel >= 10
        elif self.score_multiplier_level == 1:
            return self.steel >= 15 and self.gun_powder >= 25
        elif self.score_multiplier_level == 2:
            return self.steel >= 50
        elif self.score_multiplier_level == 3:
            return self.steel >= 25 and self.gun_powder >= 50  
        elif self.score_multiplier_level == 4:
            return self.steel >= 75
        else:
            return False

    def action_upgrade_2(self):
        self.banner_time_reduction_level += 1
        if self.banner_time_reduction_level == 1:
            self.banner_time_reduction = 600
            self.updateSteel(-10)
            self.updateGunpowder(-10)  
        elif self.banner_time_reduction_level == 2:
            self.banner_time_reduction = 1200
            self.updateGunpowder(-25)  
        elif self.banner_time_reduction_level == 3:
            self.banner_time_reduction = 1800
            self.updateSteel(-25)
        return 0

    def mask_upgrade_2(self):
        if self.banner_time_reduction_level == 0:
            return self.steel >= 10 and self.gun_powder >= 10
        elif self.banner_time_reduction_level == 1:
            return self.gun_powder >= 25
        elif self.banner_time_reduction_level == 2:
            return self.steel >= 25
        else:
            return False
        
    def action_upgrade_3(self):
        self.iron_cap_multiplier_level += 1
        if self.iron_cap_multiplier_level == 1:
            self.iron_cap_multiplier = 1.5
            self.ore_cap = 150000
            self.updateSteel(-10)
        elif self.iron_cap_multiplier_level == 2:
            self.iron_cap_multiplier = 2
            self.ore_cap = 200000
            self.updateGunpowder(-20)            
        elif self.iron_cap_multiplier_level == 3:
            self.iron_cap_multiplier = 2.5
            self.ore_cap = 250000
            self.updateSteel(-25) 
        elif self.iron_cap_multiplier_level == 4:
            self.iron_cap_multiplier = 3
            self.ore_cap = 300000
            self.updateSteel(-25)
            self.updateGunpowder(-25)
        elif self.iron_cap_multiplier_level == 5:
            self.iron_cap_multiplier = 4
            self.ore_cap = 400000
            self.updateSteel(-50)
        return 0
    
    def mask_upgrade_3(self):
        if self.iron_cap_multiplier_level == 0:
            return self.steel >= 10
        elif self.iron_cap_multiplier_level == 1:
            return self.gun_powder >= 20
        elif self.iron_cap_multiplier_level == 2:
            return self.steel >= 25
        elif self.iron_cap_multiplier_level == 3:
            return self.gun_powder >= 25 and self.steel >= 25
        elif self.iron_cap_multiplier_level == 4:
            return self.steel >= 50
        else:
            return False

    def action_upgrade_4(self):
        self.weapon_damage_multiplier_level += 1
        if self.weapon_damage_multiplier_level == 1:
            self.weapon_damage_multiplier = 1.25
            self.updateGunpowder(-15)  
        elif self.weapon_damage_multiplier_level == 2:
            self.weapon_damage_multiplier = 1.5
            self.updateSteel(-15)  
        elif self.weapon_damage_multiplier_level == 3:
            self.weapon_damage_multiplier = 2
            self.updateGunpowder(-20)  
            self.updateSteel(-10)
        return 0
    
    def mask_upgrade_4(self):
        if self.weapon_damage_multiplier_level == 0:
            return self.gun_powder >= 15
        elif self.weapon_damage_multiplier_level == 1:
            return self.steel >= 15
        elif self.weapon_damage_multiplier_level == 2:
            return self.steel >= 10 and self.gun_powder >= 20
        else:
            return False

    def action_upgrade_5(self):
        self.cannon_damage_multiplier_level += 1
        if self.cannon_damage_multiplier_level == 1:
            self.cannon_damage_multiplier = 1.25
            self.updateGunpowder(-25)  
        elif self.cannon_damage_multiplier_level == 2:
            self.cannon_damage_multiplier = 1.5
            self.updateSteel(-10)
            self.updateGunpowder(-20) 
        elif self.cannon_damage_multiplier_level == 3:
            self.cannon_damage_multiplier = 2
            self.updateSteel(-25)
        return 0
    
    def mask_upgrade_5(self):
        if self.cannon_damage_multiplier_level == 0:
            return self.gun_powder >= 25
        elif self.cannon_damage_multiplier_level == 1:
            return self.steel >= 10 and self.gun_powder >= 20
        elif self.cannon_damage_multiplier_level == 2:
            return self.steel >= 25
        else:
            return False

    def action_upgrade_6(self):
        self.bomb_damage_multiplier_level += 1
        if self.bomb_damage_multiplier_level == 1:
            self.bomb_damage_multiplier = 1.25
            self.updateGunpowder(-10)  
            self.updateSteel(-10)
        elif self.bomb_damage_multiplier_level == 2:
            self.bomb_damage_multiplier = 1.5
            self.updateGunpowder(-30) 
        elif self.bomb_damage_multiplier_level == 3:
            self.bomb_damage_multiplier = 2
            self.updateSteel(-30)
        return 0

    def mask_upgrade_6(self):
        if self.bomb_damage_multiplier_level == 0:
            return self.gun_powder >= 10 and self.steel > 10
        elif self.bomb_damage_multiplier_level == 1:
            return self.gun_powder >= 30
        elif self.bomb_damage_multiplier_level == 2:
            return self.steel >= 30
        else:
            return False

    def action_purchase_trade_1(self):
        from Models.Decoy import MusketeerDecoy, WarriorDecoy
        from Models.Furance import Furance
        if self.day == 1:
            self.addToInventory(MusketeerDecoy())
            self.updateGunpowder(-5)
        elif self.day == 2:
            self.addToInventory(WarriorDecoy())
            self.updateGunpowder(-15)
        elif self.day == 3:
            self.addToInventory(Furance(3))
            self.updateGunpowder(-40)
        self.trade_1 = False
        return 1
    
    def mask_trade_1(self):
        res = self.trade_1
        if self.day == 1:
            res = res and self.gun_powder >= 5
        elif self.day == 2:
            res = res and self.gun_powder >= 15
        elif self.day == 3:
            res = res and self.gun_powder >= 40
        return res

    def action_purchase_trade_2(self):
        from Models.Resource import SteelPile
        from Models.Furance import Furance
        from Models.Alchemy import AlchemyTable
        if self.day == 1:
            self.addToInventory(SteelPile(3))
            self.updateGunpowder(-25)
        elif self.day == 2:
            self.addToInventory(Furance(3))
            self.updateGunpowder(-25)
        elif self.day == 3:
            self.addToInventory(AlchemyTable(1))
            self.updateSteel(-30)
        self.trade_2 = False
        return 1
    
    def mask_trade_2(self):
        res = self.trade_2
        if self.day == 1:
            res = res and self.gun_powder >= 25
        elif self.day == 2:
            res = res and self.gun_powder >= 25
        elif self.day == 3:
            res = res and self.steel >= 30
        return res

    def action_purchase_trade_3(self):
        from Models.Anvil import Anvil
        from Models.Decoy import BattleMageDecoy
        from Models.Cannon import Cannon
        if self.day == 1:
            self.addToInventory(Anvil(2))
            self.updateSteel(-40)
        elif self.day == 2:
            self.addToInventory(BattleMageDecoy())
            self.updateSteel(-25)
        elif self.day == 3:
            self.addToInventory(Cannon(5))
            self.updateSteel(-60)
        self.trade_3 = False
        return 1
    
    def mask_trade_3(self):
        res = self.trade_3
        if self.day == 1:
            res = res and self.steel >= 40
        elif self.day == 2:
            res = res and self.steel >= 25
        elif self.day == 3:
            res = res and self.steel >= 60
        return res

    def action_purchase_trade_4(self):
        from Models.Cannon import Cannon
        from Models.Resource import SteelPile
        from Models.Decoy import BattleMageDecoy
        if self.day == 1:
            self.addToInventory(Cannon(2))
        elif self.day == 2:
            self.addToInventory(SteelPile(3))
        elif self.day == 3:
            self.addToInventory(BattleMageDecoy())
        self.trade_4 = False
        return 1
    
    def mask_trade_4(self):
        return self.trade_4
    

    # UTILITIES
    def updateDay(self):
        self.day += 1
        self.trade_1 = True
        self.trade_2 = True
        self.trade_3 = True
        self.trade_4 = True

    def updateScore(self, score):
        self.score = int(self.score + (score * self.score_multiplier))

    def updateSteel(self, steel):
        self.steel = self.steel + steel
    
    def updateGunpowder(self, gun_powder):
        self.gun_powder = self.gun_powder + gun_powder

    def updateOre(self, ore):
        new_ore = self.ore + ore
        if new_ore > self.ore_cap:
            self.ore = self.ore_cap
        else:
            self.ore = new_ore
        
    def updateKillCount(self):
        self.invaders_killed += 1
    
    def updateActionsTaken(self):
        self.actions_taken += 1

    def getResources(self):
        return self.banners + self.ironCrates + self.gunpowderPile + self.steelPile
    
    def getInvaders(self):
        invaders = (self.flagGrunts + 
                    self.spearGrunts + 
                    self.swordGrunts + 
                    self.musketeers + 
                    self.warriors +
                    self.battlemages)
        invaders = sorted(invaders, key=lambda i : i.health)
        return invaders
    
    def getStructures(self):
        return self.anvils + self.furances + self.cannons + self.alchemyTables
    
    def getMisc(self):
        return (self.musketeerParts + 
                self.musketeerDecoys + 
                self.warriorParts + 
                self.warriorDecoys +
                self.battlemageDecoys)

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
                len(self.ironCrates) +
                len(self.banners) +
                len(self.flagGrunts) +
                len(self.spearGrunts) +
                len(self.swordGrunts) +
                len(self.alchemyTables) +
                len(self.bombs) +
                len(self.battlemageDecoys) +
                len(self.battlemages))

    def render(self):
        print("------------------------------------------------------------------------------------------------------")
        print(f"Score\t\t\t{self.score}\tStructures\t\t{self.getStructures()}")
        print(f"Ore\t\t\t{self.ore}\tResources\t\t{self.getResources()}")
        print(f"Gunpowder\t\t{self.gun_powder}\tInvaders\t\t{self.getInvaders()}")
        print(f"Steel\t\t\t{self.steel}\tParts & Decoys\t\t{self.getMisc()}")
        print(f"GP Collected\t\t{self.gp_collected}\tWeapons\t\t\t{self.weapons + self.bombs}")
        print(f"Steel Collected\t\t{self.s_collected}\tInvaders Killed\t\t{self.invaders_killed}" )
        print(f"Action Taken\t\t{self.actions_taken}\tBoard Occupied\t\t{self.getBoardOccupied()}")
        print(f"Discarded\t\t{self.discard}\tBanner\t\t\t{self.banner_holder.getStock()}")
        print(f"Upgrades", self.score_multiplier_level, 
              self.banner_time_reduction_level, 
              self.iron_cap_multiplier_level,
              self.weapon_damage_multiplier_level,
              self.cannon_damage_multiplier_level,
              self.bomb_damage_multiplier_level)
        print(f"Day {self.day}")
        print("------------------------------------------------------------------------------------------------------")

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
        user_input = int(user_input)
        if user_input == -1:
            break
        else:
            print("Reward received:", g1.perform_action(user_input),"\n")