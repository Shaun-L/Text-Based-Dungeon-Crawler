import goblin
import ogre
import troll
import random
import enemy_factory

class ExpertFactory(enemy_factory.EnemyFactory):
  """Represents a factory that creates and returns the expert level enemies inheriting from the enemy_factory interface"""
  def create_random_enemy(self):
    """Overrides abstract method and randomly returns an expert enemy between the goblin, ogre, or troll."""
    enemies = [goblin.AngryGoblin(), ogre.HorribleOgre(), troll.Troll()]
    return random.choice(enemies)
    