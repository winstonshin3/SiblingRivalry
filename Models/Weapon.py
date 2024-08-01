class Weapon:
    weapon_damage_map = {0:0, 1:100, 2:250, 3:750, 4:2000, 5:5000, 6:12500}

    def __init__(self, level):
        self.level = level
        self.description = f"Weapon {self.level}"
    
    def __repr__(self):
        return self.description

    def getDamage(self):
        return Weapon.weapon_damage_map[self.level]

    def getLevel(self):
        return self.level
    
    @classmethod
    def mergeWeapon(cls, w1, w2):
        if w1.getLevel() != w2.getLevel() or w1.getLevel() >= 6:
            return [w1,w2]
        if w1.getLevel() < 6:
            return [cls(w1.getLevel() + 1)]
