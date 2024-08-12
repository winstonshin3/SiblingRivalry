class AlchemyTable:
    alchemytable_cost_map = {1:5, 2:7, 3:10}

    def __init__(self, level):
        self.level = level

    def __repr__(self):
        return f"A{self.level}"
    
    def getUpgrade(self):
        return AlchemyTable(self.level + 1)
    
    def getCost(self):
        return AlchemyTable.alchemytable_cost_map[self.level]
    
    def getLevel(self):
        return self.level
    
    def tapProduction(self):
        if self.level == 1:
            return Bomb(0)
        elif self.level == 2:
            return Bomb(1)
        elif self.level == 3:
            return Bomb(2)
        
class Bomb:
    bomb_damage_map = {0:0, 1:0, 2:0, 3:25000, 4:75000}
    def __init__(self, level):
        self.level = level

    def __repr__(self):
        return f"B{self.level}"
    
    def getUpgrade(self):
        return Bomb(self.level + 1)
    
    def getLevel(self):
        return self.level
    
    def getDamage(self):
        return Bomb.bomb_damage_map[self.level]

if __name__ == "__main__":
    a1 = AlchemyTable(1)
    a2 = AlchemyTable(2)
    a3 = AlchemyTable(3)

    bombs = []
    bombs.append(a1.tapProduction())
    bombs.append(a2.tapProduction())
    bombs.append(a3.tapProduction())
    print(bombs)