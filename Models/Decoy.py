from Invader import Musketeer, Warrior, BattleMage

class MusketeerDecoy():    
    def __init__(self):
        self.description = "Musketeer Decoy"
        pass

    def tapToSummon(self):
        return Musketeer()

class WarriorDecoy():
    def __init__(self):
        self.description = "Warrior Decoy"
        pass

    def tapToSummon(self):
        return Warrior()
        
class BattleMageDecoy():
    def __init__(self):
        pass

    def tapToSummon(self):
        return BattleMage()
    
# Tests
# md = MusketeerDecoy()
# m = md.tapToSummon()
# print(m.score)