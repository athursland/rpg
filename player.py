# name: Ali Thursland
# date: 2019-11-17
# title: Text-based RPG

import objects

class Player:
    def __init__(self):
        self.inventory = [objects.Pipe(), objects.BronxKnife(), 'Gold(5)', 'Crusty Bread']

    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print('* ' + str(item))

    def __str__(self):
        return "Name: " + self.name \
        + " Age: " + str(self.age) \
        + " Gender: " + self.gender
