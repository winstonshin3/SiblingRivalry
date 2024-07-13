class Anvil:
    anvil_cost_map = {1:250, 2:500, 3:750, 4:1000, 5:1500}

    def __init__(self, level):
        self.level = level

    def tapProduction(self):
        pass
    
    @classmethod
    def mergeAnvil(cls, w1, w2):
        if w1.getLevel() != w2.getLevel():
            return [w1,w2]
        
        if w1.getLevel() < 4:
            return cls(w1.getLevel() + 1)
        else:
            return cls(w1.getLevel())

