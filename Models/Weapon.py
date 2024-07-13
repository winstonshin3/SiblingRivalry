class Weapon:
    weapon_damage_map = {0:0, 1:100, 2:250, 3:750, 4:2000, 5:5000, 6:12500}

    def __init__(self, level):
        self.level = level

    def getDamage(self):
        return Weapon.weapon_damage_map[self.level]
    
    @classmethod
    def mergeWeapon(cls, w1, w2):
        if w1.getLevel() != w2.getLevel():
            return [w1,w2]
        
        if w1.getLevel() < 6:
            return cls(w1.getLevel() + 1)
        else:
            return cls(w1.getLevel())