import entity
import random

class HorribleOgre(entity.Entity):
  """Represents the 'Expert Ogre' enemy inheriting from the entity class
  Attributes:
    _name (str) = name of the entity
    _hp (int) = hitpoints that can change
    _max_hp (int) = the characters max hitpoints
    """

  def __init__(self):
    '''Initializing the name and max_hp variables by using super()'''
    super().__init__("Horrible Ogre", random.randint(8,12))

  def attack(self, entity):
    '''Overriding the abstract attack method, taking in the entity, and dealing damage randomly between 6-10. Then it returns the string explaining what happened to the user.'''
    rand = random.randint(6,10)
    entity.take_damage(rand)
    return self.name + " attacks "+entity.name +" for " +str(rand) + " damage!"