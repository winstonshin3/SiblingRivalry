class Resource():
    def __init__(self, level):
        self.level = level

    def getLevel(self):
        return self.level

class IronCrate(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"Iron Crate {self.level}"

    def getResourceValue(self):
        if self.level == 1:
            return 5000
        elif self.level == 2:
            return 12000
        
    @classmethod
    def mergeResource(cls, r1, r2):
        if r1.getLevel() != r2.getLevel() or r1.getLevel() >= 2 or r2.getLevel() >=2:
            return [r1,r2]
        return [cls(r1.getLevel() + 1)]

class GunpowderPile(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"Gunpowder Pile {self.level}"

    def getResourceValue(self) -> int:
        if self.level == 1:
            return 2
        elif self.level == 2:   
            return 5
        elif self.level == 3:
            return 12
        elif self.level == 4:
            return 30
        
    @classmethod
    def mergeResource(cls, r1, r2):
        if r1.getLevel() != r2.getLevel() or r1.getLevel() >= 4 or r2.getLevel() >= 4:
            return [r1,r2]
        return [cls(r1.getLevel() + 1)]

class SteelPile(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"Steel Pile {self.level}"

    def getResourceValue(self):
        if self.level == 1:
            return 2
        elif self.level == 2:   
            return 5
        elif self.level == 3:
            return 12
        elif self.level == 4:
            return 30
    
    @classmethod
    def mergeResource(cls, r1, r2):
        if r1.getLevel() != r2.getLevel() or r1.getLevel() >= 4 or r2.getLevel() >= 4:
            return [r1,r2]
        return [cls(r1.getLevel() + 1)]

