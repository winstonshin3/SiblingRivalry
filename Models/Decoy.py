class MusketeerDecoy():    
    def __init__(self):
        self.description = "Musketeer Decoy"
        pass

    def tapToSummon(self):
        from Invader import Musketeer
        return Musketeer()

class WarriorDecoy():
    def __init__(self):
        self.description = "Warrior Decoy"
        pass

    def tapToSummon(self):
        from Invader import Warrior
        return Warrior()
        
class BattleMageDecoy():
    def __init__(self):
        self.description = "BattleMage Decoy"
        pass

    def tapToSummon(self):
        from Invader import BattleMage
        return BattleMage()
    
# Tests

if __name__ == "__main__":
    md = MusketeerDecoy()
    m = md.tapToSummon()
    print(m.score)