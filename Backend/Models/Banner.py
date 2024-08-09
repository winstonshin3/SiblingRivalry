class Banner:
    def __init__(self):
        self.level = 0

    def __repr__(self):
        return f"B{self.level}"
    
    def getLevel(self):
        return self.level

    def tap(self):
        from Models.Invader import FlagGrunt, SpearGrunt, SwordGrunt
        self.level += 1
        if self.level == 1:
            return FlagGrunt()
        elif self.level == 2:
            return SpearGrunt()
        elif self.level == 3:
            return SwordGrunt()
        else:
            return SwordGrunt()
        
    
class BannerHolder:
    def __init__(self):
        self.stock = 5
    
    def restock(self):
        self.stock += 1

    def tap(self):
        self.stock -= 1
        return Banner()
    
    def getStock(self):
        return self.stock

        
        
    
