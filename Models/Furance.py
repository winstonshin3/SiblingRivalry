class Furance:
    ore_production_map = {1:3, 2:5, 3:8, 4:15, 5:25}

    def __init__(self, level):
        self.level = level
    
    def produceOre(self) -> int:
        return Furance.ore_production_map[self.level]
    
    def getLevel(self):
        return self.level
    
    @classmethod
    def mergeFurance(cls, f1, f2):
        if f1.getLevel() != f2.getLevel():
            return [f1,f2]
        
        if f1.getLevel() < 4:
            return cls(f1.getLevel() + 1)
        else:
            return cls(f1.getLevel())
        


f1 = Furance(3)
f2 = Furance(3)
f3 = Furance.mergeFurance(f1,f2)
print(f1.level)
print(f2.level)
print(f3.level)