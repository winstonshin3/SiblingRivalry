class InvaderPart:
    def __init__(self, level):
        self.level = level
    
    def getLevel(self):
        return self.level
    

class MusketeerPart(InvaderPart):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"MP{self.level}"

    def __repr__(self):
        return self.description

    def getUpgrade(self):
        from Models.Decoy import MusketeerDecoy
        if self.level < 4:
            return MusketeerPart(self.level + 1)
        else:
            return MusketeerDecoy() 
    

class WarriorPart(InvaderPart):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"WP{self.level}"
    
    def __repr__(self):
        return self.description
    
    def getUpgrade(self):
        from Models.Decoy import WarriorDecoy
        if self.level < 4:
            return WarriorPart(self.level + 1)
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