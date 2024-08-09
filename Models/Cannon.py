class Cannon:
    cannon_damage_map = {1:100, 2:180, 3:320, 4:560, 5:1000}

    def __init__(self, level):
        self.level = level
    
    def __repr__(self):
        return f"C{self.level}"
    
    def getLevel(self):
        return self.level
    
    def getUpgrade(self):
        return Cannon(self.level + 1)
    
    def getDamage(self):
        return Cannon.cannon_damage_map[self.level]