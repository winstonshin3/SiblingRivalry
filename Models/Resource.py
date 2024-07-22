class Resource():
    def __init__(self, level):
        self.level = level

class IronCrate(Resource):
    def __init__(self, level):
        super().__init__(level)
        self.description = f"Iron Crate {self.level}"

    def getResourceValue(self):
        if self.level == 1:
            return 5000
        elif self.level == 2:
            return 12000

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

