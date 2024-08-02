class MusketeerDecoy():    
    def __init__(self):
        self.description = "MD"
        pass

    def __repr__(self):
        return self.description

    def tapToSummon(self):
        from Models.Invader import Musketeer
        return Musketeer()

class WarriorDecoy():
    def __init__(self):
        self.description = "WD"
        pass

    def __repr__(self):
        return self.description

    def tapToSummon(self):
        from Models.Invader import Warrior
        return Warrior()
        
class BattleMageDecoy():
    def __init__(self):
        self.description = "BD"
        pass

    def __repr__(self):
        return self.description

    def tapToSummon(self):
        from Invader import BattleMage
        return BattleMage()
    
# Tests

if __name__ == "__main__":
    md = MusketeerDecoy()
    m = md.tapToSummon()
    print(m.score)