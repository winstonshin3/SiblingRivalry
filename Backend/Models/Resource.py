class Resource():
    def __init__(self, level):
        self.level = level

    def getLevel(self):
        return self.level

class IronCrate(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"IC{self.level}"

    def __repr__(self):
        return self.description

    def getResourceValue(self):
        if self.level == 1:
            return 5000
        elif self.level == 2:
            return 12000
        
    def getUpgrade(self):
        return IronCrate(self.level + 1)

class GunpowderPile(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"GP{self.level}"

    def __repr__(self):
        return self.description

    def getResourceValue(self) -> int:
        if self.level == 1:
            return 2
        elif self.level == 2:   
            return 5
        elif self.level == 3:
            return 12
        elif self.level == 4:
            return 30
    
    def getUpgrade(self):
        return GunpowderPile(self.level + 1)

class SteelPile(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"SP{self.level}"

    def __repr__(self):
        return self.description

    def getResourceValue(self):
        if self.level == 1:
            return 2
        elif self.level == 2:   
            return 5
        elif self.level == 3:
            return 12
        elif self.level == 4:
            return 30
    
    def getUpgrade(self):
        return SteelPile(self.level + 1)

