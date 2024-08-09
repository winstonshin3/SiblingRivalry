class Furance:
    ore_production_map = {1:3, 2:5, 3:8, 4:15, 5:25}

    def __init__(self, level):
        self.level = level

    def __repr__(self):
        return f"F{self.level}"
    
    def produceOre(self) -> int:
        return Furance.ore_production_map[self.level]
    
    def getLevel(self):
        return self.level
    
    def getUpgrade(self):
        return Furance(self.level + 1)
    
    
# Test

if __name__ == "__main__":
    f1 = Furance(6)
    f2 = Furance(6)
    f3 = Furance.mergeFurance(f1,f2)
    print(f1.level)
    print(f2.level)
    print(len(f3))

    