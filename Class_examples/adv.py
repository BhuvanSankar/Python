
# characters
#   name
#   health/armour ...
#   gender
#   level
#   items
#
#   take/drop items
#   move


# item
#   name


# room
#    name
#    items
#    characters
#    adjacent rooms
#
#    add/remove item and character


class Item(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return "Item({0})".format(self._name)

knife = Item('knife')
remote = Item('remote')
chilli = Item('chilli')

class Room(object):
    def __init__(self, name, items):
        self._name = name
        self._items = items
        self._chars = []
        self._adj = []

    def set_adj(self, rooms):
        self._adj = rooms

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:              # Changed
            self._items.remove(item)
            return True
        return False

    def is_adj(self, room):
        return room in self._adj
        
    def add_char(self, char):
        self._chars.append(char)

    def remove_char(self, char):
        self._chars.remove(char)

    def __str__(self):
        return self._name

    def __repr__(self):
        return "Name: {0}, Items: {1}, Chars: {2}".\
            format(self._name, self._items, self._chars)
    
        

kitchen = Room('kitchen', [knife])
lounge = Room('lounge', [remote])
bathroom = Room('bathroom', [])

kitchen.set_adj([lounge])
lounge.set_adj([kitchen, bathroom])

class Character(object):
    def __init__(self, name, items, room):
        self._name = name
        self._items = items
        self._room = room
        room.add_char(self)
    
    def __str__(self):
        return self._name

    def __repr__(self):
        return "Name: {0}, Items: {1}, Room: {2}".\
            format(self._name, self._items, str(self._room))  ## NOTE str

    def drop(self, item):
        if item in self._items:
            self._items.remove(item)
            self._room.add_item(item)   # !

    def take(self, item):
        if self._room.remove_item(item):
            self._items.append(item)

    def move(self, room):
        if self._room.is_adj(room):
            room.add_char(self)
            self._room.remove_char(self)
            self._room = room

fred = Character('Fred', [], kitchen) 
    
