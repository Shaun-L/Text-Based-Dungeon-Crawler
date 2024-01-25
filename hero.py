import entity
import random


class Hero(entity.Entity):
  """Represents a hero character in the game inheriting from entity
  Attributes:
    _name (str) = name of the entity
    _hp (int) = hitpoints that can change
    _max_hp (int) = the characters max hitpoints
    _loc (int []) = a list that holds two values, the x and y coordinates of the character
    """

  def __init__(self, name, max_hp):
    """takes the name and max_hp and intializes the name, max hp and hp(changes). Also sets the starting location to (0,0)"""
    super().__init__(name, max_hp)
    self._loc = [0,0]

  @property
  def loc(self):
    '''returns the location'''
    return self._loc

  def attack(self, entity):
    '''Takes in the entity being attacked, attacks the entity for a random number from 2 to 5. Then returns a string describing what happened'''
    rand = random.randint(2,5)
    entity.take_damage(rand)
    return self.name + " attacks the "+entity.name +" for " +str(rand) + " damage!"

  def go_north(self):
    """Returns 'x' if location is out of bounds, if not, changes and returns the location to 1 unit north."""
    if self._loc[0] > 0:
      self._loc[0] -= 1
      return self.loc
    else:
      return 'x'
      
  def go_south(self):
    """Returns 'x' if location is out of bounds, if not, changes and returns the location to 1 unit south."""
    if self._loc[0] < 4:
      self._loc[0] += 1
      return self.loc
    else:
      return 'x'
      
  def go_west(self):
    """Returns 'x' if location is out of bounds, if not, changes and returns the location to 1 unit west."""
    if self._loc[1] > 0:
      self._loc[1] -= 1
      return self.loc
    else:
      return 'x'
      
  def go_east(self):
    """Returns 'x' if location is out of bounds, if not, changes and returns the location to 1 unit east."""
    if self._loc[1] < 4:
      self._loc[1] += 1
      return self.loc
    else:
      return 'x'    