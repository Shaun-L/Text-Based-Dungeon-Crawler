import entity
import random

class Troll(entity.Entity):
  """Represents the 'Expert Troll' enemy inheriting from the entity class
  Attributes:
    _name (str) = name of the entity
    _hp (int) = hitpoints that can change
    _max_hp (int) = the characters max hitpoints
    """

  def __init__(self):
    '''Initializing the name and max_hp variables by using super()'''
    super().__init__("Sarcastic Troll", random.randint(10,14))

  def attack(self, entity):
    '''Overriding the abstract attack method, taking in the entity, and dealing damage randomly between 8-12. Then it returns the string explaining what happened to the user.'''
    rand = random.randint(8,12)
    entity.take_damage(rand)
    return self.name + " attacks "+entity.name +" for " +str(rand) + " damage!"