class Weapon:
    weapon_damage_map = {0:0, 1:100, 2:250, 3:750, 4:2000, 5:5000, 6:12500}

    def __init__(self, level):
        self.level = level
        self.description = f"W{self.level}"
    
    def __repr__(self):
        return self.description

    def getDamage(self):
        return Weapon.weapon_damage_map[self.level]

    def getLevel(self):
        return self.level
    
    def getUpgrade(self):
        return Weapon(self.level + 1)
    
