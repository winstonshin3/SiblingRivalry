class InvaderPart:
    def __init__(self, level):
        self.level = level
    
    def getLevel(self):
        return self.level

class MusketeerPart(InvaderPart):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"Musketeer Part {self.level}"
    
    @classmethod
    def mergePart(cls, f1, f2):
        from Models.Decoy import MusketeerDecoy
        if f1.getLevel() != f2.getLevel():
            return [f1,f2]
        
        if f1.getLevel() < 4:
            return cls(f1.getLevel() + 1)
        else:
            return MusketeerDecoy()

class WarriorPart(InvaderPart):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"Warrior Part {self.level}"

    @classmethod
    def mergePart(cls, f1, f2):
        from Models.Decoy import WarriorDecoy
        if f1.getLevel() != f2.getLevel():
            return [f1,f2]
        
        if f1.getLevel() < 4:
            return cls(f1.getLevel() + 1)
        else:
            return WarriorDecoy()

#Tests

if __name__ == "__main__":
    mp1 = MusketeerPart(2)
    wp1 = WarriorPart(5)
    wp2 = WarriorPart(5)
    wd = WarriorPart.mergePart(wp1, wp2)

    print(mp1.description)
    print(wd.description)