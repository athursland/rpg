# name: Ali Thursland
# date: 2019-11-17
# title: Text-based RPG

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class BrokenGlassBottle(Weapon):
    def __init__(self):
        self.name = "Broken glass bottle"
        self.description = "Looks like Dos Equis. Surely makes for the most interesting weapon in the world."
        self.damage = 4

class Pipe(Weapon):
    def __init__(self):
        self.name = "Pipe"
        self.description = "A twelve-inch metal pipe, suitable for sparring."
        self.damage = 5

class BronxKnife(Weapon):
    def __init__(self):
        self.name = "Bronx Knife"
        self.description = "Don't be caught dead in the boogie down borough without one, or you'l be sorry."
        self.damage = 8
