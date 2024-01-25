import easy_goblin
import easy_ogre
import easy_troll
import random
import enemy_factory

class BeginnerFactory(enemy_factory.EnemyFactory):
  """Represents a factory that creates and returns the beginner level enemies inheriting from the enemy_factory inteface"""
  def create_random_enemy(self):
    """Overrides abstract method and randomly returns an easy enemy between the goblin, ogre, or troll."""
    enemies = [easy_goblin.EasyGoblin(), easy_ogre.EasyOgre(), easy_troll.EasyTroll()]
    return random.choice(enemies)
    
    