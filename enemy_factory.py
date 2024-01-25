import abc
class EnemyFactory(abc.ABC):
  """Abstract interface class representing a factory creating enemy entities."""
  @abc.abstractmethod
  def create_random_enemy(self):
    """Abstract method that will be overrident to create a random enemy."""
    pass

  
  