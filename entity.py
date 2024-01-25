import abc
class Entity(abc.ABC):
  """Abstract class that represents a character in the game
  Attributes:
    _name (str) = name of the entity
    _hp (int) = hitpoints that can change
    _max_hp (int) = the characters max hitpoints
    """

  def __init__(self, name, max_hp):
    """takes the name and max_hp and intializes the name, max hp and hp(changes)"""
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  
  @property
  def name(self):
    '''returns name'''
    return self._name

  @property
  def hp(self):
    '''returns hp'''
    return self._hp

  def take_damage(self, dmg):
    """takes the damage number and subtracts that from the hp, also checks to make sure hp cant go below 0"""
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0

  def heal(self):
    """the function heals the characters hitpoints to their maximum"""
    self._hp = self._max_hp
      

  def __str__(self):
    """returns the name, hp/max hp of the entity."""
    return str(self._name)+"\nHP: "+str(self._hp)+"/"+str(self._max_hp)

  @abc.abstractmethod
  def attack(self, entity):
    """abstract method that differs between entities"""
    pass
    

  