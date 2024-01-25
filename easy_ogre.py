import entity
import random

class EasyOgre(entity.Entity):
  """Represents the 'Easy Ogre' enemy inheriting from the entity class
  Attributes:
    _name (str) = name of the entity
    _hp (int) = hitpoints that can change
    _max_hp (int) = the characters max hitpoints
    """

  def __init__(self):
    '''Initializing the name and max_hp variables by using super()'''
    super().__init__("Ogre", random.randint(3,5))

  def attack(self, entity):
    '''Overriding the abstract attack method, taking in the entity, and dealing damage randomly between 1-4. Then it returns the string explaining what happened to the user.'''
    rand = random.randint(1,4)
    entity.take_damage(rand)
    return self.name + " attacks "+entity.name +" for " +str(rand) + " damage!"