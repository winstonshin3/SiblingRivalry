class InvaderPart:
    def __init__(self, level):
        self.level = level

    @classmethod
    def InvaderPart(cls, f1, f2):
        if f1.getLevel() != f2.getLevel():
            return [f1,f2]
        
        if f1.getLevel() < 4:
            return cls(f1.getLevel() + 1)
        else:
            return cls(f1.getLevel())

class MusketeerPart(InvaderPart):
    @classmethod
    def mergePart(cls, f1, f2):
        if f1.getLevel() != f2.getLevel():
            return [f1,f2]
        
        if f1.getLevel() < 4:
            return cls(f1.getLevel() + 1)
        else:
            return cls(f1.getLevel())

class WarriorPart(InvaderPart):
    @classmethod
    def mergePart(cls, f1, f2):
        if f1.getLevel() != f2.getLevel():
            return [f1,f2]
        
        if f1.getLevel() < 4:
            return cls(f1.getLevel() + 1)
        else:
            return cls(f1.getLevel())