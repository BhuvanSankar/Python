# Item
#   Weapon is_a Item
#   Potion is_a Item

# Room

# Characters

#    Player is_a Character
#    Monster is_a Character
#      Dragon is_a Monster


import random
import math

class Item(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def use(self, char):
        """Use this item on char"""
        print("You can't do that")
        return False

    def attack(self, char1, char2):
        """char1 attacks char2 with this item"""
        print("You can't do that")
        return False   

    def __repr__(self):
        return "Item({0})".format(self._name)

    def __str__(self):
        return self._name


class HealthPotion(Item):
    def __init__(self, name, health):
        super().__init__(name)
        self._health = health

    def use(self, char):
        char.update_health(self._health)
        self._health = 0

class Sword(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self._damage = damage

    def attack(self, char1, char2):
        # modified after lecture to use a formula based on
        # char1 health to determine damage
        health = char1.get_health()
        char2.update_health(-(self._damage*math.log(health+1)/math.log(100)*random.random()))

class Room(object):
    def __init__(self, name, items):
        self._name = name
        self._adj = []
        self._items = items
        self._chars = []
        
    def get_name(self):
        return self._name

    def set_adj(self, adj):
        self._adj = adj

    def get_adj(self):
        return self._adj

    def get_items(self):
        return self._items
    
    def add_char(self, char):
        self._chars.append(char)

    def remove_char(self, char):
        self._chars.remove(char)
        
    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def __repr__(self):
        return "Room({0})".format(self._name)

    def __str__(self):
        return "Name:{0}, Items:{1}, Chars:{2}".format(self._name, self._items,
                                                       repr(self._chars))
super_food = HealthPotion("super food", 20)       
knife = Sword("knife", 40)
kitchen = Room("kitchen", [super_food, knife])


class Character(object):
    def __init__(self, name, room, items):
        self._name = name
        self._room = room
        self._items = items
        room.add_char(self)
        self._holding = None
        self._health = 100
        print("{0} is in the {1}".format(name, room.get_name()))

    def get_name(self):
        return self._name
    def get_room(self):
        return self._room
    def get_items(self):
        return self._items
    def get_health(self):
        return self._health


    def move(self, room):
        if self._room in room.get_adj():
            self._room.remove_char(self)
            room.add_char(self)
            self._room = room
            print("{0} moves to the {1}".format(self._name, room.get_name()))
            return True
        else:
            return False
        
    def drop(self, item):
        if item in self._items:
            self._items.remove(item)
            self._room.add_item(item)
            print("{0} drops {1}".format(self._name, item.get_name()))
            if self._holding == item:
                self._holding = None
            return True
        else:
            return False

    def take(self, item):
        if item in self._room.get_items():
            self._items.append(item)
            self._room.remove_item(item)
            print("{0} takes {1}".format(self._name, item.get_name()))
            return True
        else:
            return False

    def hold(self, item):
        if item in self._items:
            self._holding = item
            print("{0} holds {1}".format(self._name, item.get_name()))
            return True
        else:
            return False

    # moved up to here to show another use of super
    def attack(self, char):
        if self._holding is not None:
            h1 = char.get_health()
            self._holding.attack(self, char)
            h2 = char.get_health()
            print("{0} attacks {1} and inflicts {2:.1f} damage".\
                    format(self._name, char.get_name(), h1-h2))
            return True
        return False

    def update_health(self, health):
        self._health += health
        # don't let the health get below 0
        if self._health < 0:
            self._health = 0
        print("{0}'s health is now {1:.1f}".format(self._name, self._health))

class Player(Character):
    def __init__(self, name, room, items, health, agro):
        super().__init__(name, room, items)
        self._health = health
        self._agro = agro

    def use(self):
        if self._holding is not None:
            self._holding.use(self)
            print("{0} uses {1}".format(self._name, self._holding.get_name()))
            return True
        return False

    # changed to use Character method for attack
    def attack(self, char):
        if random.random() < self._agro:
            super().attack(char)

# add in damage
class Monster(Character):
    def __init__(self, name, room, items, health, agro, damage):
        super().__init__(name, room, items)
        self._health = health
        self._agro = agro
        self._damage = damage
        
    def attack(self, char):
        if random.random() < self._agro:
            h1 = char.get_health()
            char.update_health(-self._damage)
            h2 = char.get_health()
            print("{0} attacks {1} and inflicts {2:.1f} damage".\
                    format(self._name, char.get_name(), h1-h2))

    
fred = Player("fred", kitchen, [], 100, 0.7)
microwave = Monster("microwave", kitchen, [], 100, 1.0, 10)


print("""

+---------------------------+
|                           |
| Fred verses the microwave |
|                           |
+---------------------------+
""")

fred.take(knife)
fred.hold(knife)
while True:
    fred.attack(microwave)
    if microwave.get_health() == 0:
        print("Fred wins")
        break
    microwave.attack(fred)
    if fred.get_health() == 0:
        print("Microwave wins")
        break
    
