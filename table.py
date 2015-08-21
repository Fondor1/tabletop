__author__ = 'rakai'

from random import shuffle, choice


class Table:
    # class in/on which everything happens
    def __init__(self):
        pass

    def add_player(self):
        pass

    def remove_player(self):
        pass


class Item:
    """ Single item, e.g. a card """
    def __init__(self):
        pass


class Collection:
    """ A generic ordered grouping of items intended to be subclassed """
    def __init__(self, items=[], name='Collection'):
        self._items = items
        self._name = name

    def draw_random(self):
        """ Remove a random item from the Collection. """
        return self._items.pop(self._items.index(choice(self._items)))

    def sort(self, key=None):
        """ Sort. Optional key function. """
        self._items.sort(key=key)

    def add_item(self, item, location=None):
        """ Places new item at the location indicated """
        if location:
            self._items.insert(location, item)
        else:
            # If no location is specified, put it at the end
            self._items.append(item)

    def reorder(self, order):
        """ Reorder the top n items. Order should be an ordered list of previous item numbers
        e.g. previous Collection: ['a','b','c','d','e']. Desired order for top three items is 'c','a','b'
        passing in order=[3, 1, 2] will reorder the items in the desired configuration. """
        self._items = [self._items[item_num] for item_num in order] + self._items[len(order):]

    def draw(self, n=0):
        """ Remove the nth item from the Collection. Defaults to the top item. """
        return self._items.pop(n)

    def shuffle(self):
        """ Shuffle the Collection in place """
        shuffle(self._items)

    def peek(self, n=1):
        """ View the top n item(s) in order without removing any """
        return self._items[0:n]


class Deck(Collection):
    """ Collection of Items with specific grouping and organizational capabilities.
    The Deck is organized such that the zeroth item is considered the top item. """

    def __init__(self, items, name='Deck'):
        super().__init__()
        self._deck = items
        self._name = name


class Hand(Collection):
    # Collection of items that are only visible to one client
    def __init__(self, items):
        super().__init__()
        self._hand = items

    def draw(self, item=None):
        # Referenced item passed by name instead of index
        hand_index = self._hand.index(item)
        return self._hand.pop(hand_index)


class Player:
    # Individual to which a Hand, Deck, or Token can be assigned.
    def __init__(self, name='Player'):
        self._name = name

# TODO: Add unittests
