import entity
import random

class AngryGoblin(entity.Entity):
  """Represents the 'Expert Goblin' enemy inheriting from the entity class
  Attributes:
    _name (str) = name of the entity
    _hp (int) = hitpoints that can change
    _max_hp (int) = the characters max hitpoints
    """

  def __init__(self):
    '''Initializing the name and max_hp variables by using super()'''
    super().__init__("Angry Goblin", random.randint(6,10))

  def attack(self, entity):
    '''Overriding the abstract attack method, taking in the entity, and dealing damage randomly between 4-8. Then it returns the string explaining what happened to the user.'''
    rand = random.randint(4,8)
    entity.take_damage(rand)
    return self.name + " attacks "+entity.name +" for " +str(rand) + " damage!"