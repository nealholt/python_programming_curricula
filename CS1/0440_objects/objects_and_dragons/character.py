
class Character:
    def __init__(self, name, role):
        '''Create a player character with the given name and role.'''
        self.name = name
        if role == "wizard":
            self.magic = 3
            self.strength = 1
            self.stealth = 2
        elif role == "rogue":
            self.magic = 2
            self.strength = 1
            self.stealth = 3
        elif role == "warrior":
            self.magic = 1
            self.strength = 3
            self.stealth = 2
        else:
            print('"'+role+'" is not a typical role. You must be a peasant.')
            self.magic = 1
            self.strength = 1
            self.stealth = 1

    def castSpell(self, target):
        '''Cast a spell on the target.'''
        if self.magic == 3:
            target.hp = target.hp-1
            print("Your spell damages the dragon.")
        else:
            print("Your spell has no effect.")

    def swingSword(self, target):
        '''Swing your sword at the target.'''
        if self.strength == 3:
            target.hp = target.hp-1
            print("Your sword damages the dragon.")
        else:
            print("Your sword has no effect.")

    def sneakAttack(self, target):
        '''Perform a sneak attack on the target.'''
        if self.stealth == 3:
            target.hp = target.hp-1
            print("You sneak up and stab the dragon.")
        else:
            print("You are discovered and must run away.")

