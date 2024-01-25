
class Map:
  """Represents the map for the game:
  Attributes:
    _instance (class var) = used to create the one time object for the class
    _initialized (class var) = used to create the one time attributes for the class that can only be modified and not remade from scratch
    _map (char[][]): A 2D list that reads from map.txt to append each space accordingly to the correct letter
    _revealed (boolean[][]): A 2D list filled with False values with the same dimensions as the map. """
  _instance = None
  _initialized = False

  def __new__(cls):
    """Creates the one time object for the class"""
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    """Creates the map and revealed 2D lists once that will then be modified but not remade using the load_map function"""
    if not Map._initialized:
        
      self._map = []
      self._revealed = []
      self.load_map(1)
      
      Map._initialized = True
      

  def __getitem__(self,row):
    """returns the specified row from the map, and can also return the column"""
    return self._map[row]

  def __len__(self):
    """returns the length of the map"""
    return len(self._map)

  def load_map(self, map_num):
    """Takes in the map number, and 'loads' that maps by reading it from a file as well as resets the values of _revealed to all false."""

    #Makes the self._map variable blank before opening the correct map file and appending each letter into a the 2D list
    self._map = []
    
    file = open("map"+str(map_num)+".txt")
    lines = file.readlines()
    list = []
    for i in range(5):
      list.append(lines[i].strip())
    self._map = []
    for line in list:
      inside = []
      for letter in line:
        inside.append(letter)
      self._map.append(inside)
    file.close()

    #Makes the self._revealed varaible blank before filling it back up with all False values.
    self._revealed = []
    for i in range(5):
      list = []
      for j in range(5):
        list.append(False)
      self._revealed.append(list)

    

  def show_map(self, loc):
    """Takes in the users location, and prints a map showing each revealed space, hiding all the places not revealed, as well as the players location."""

    for row in range(5):
      for item in range(5):
        place = [row,item]
        if loc == place:
          print('*', end = ' ')
        elif not self._revealed[row][item]:
          print('x', end = ' ')
        else:
          print(self._map[row][item], end = ' ')
      print()

  def reveal(self,loc):
    """takes in the given location and switches the False in the _revealed variable to True at the location."""
    self._revealed[loc[0]][loc[1]] = True
    
  def remove_at_loc(self,loc):
    """Takes in the given location and turns the letter on the map into 'n'."""
    self._map[loc[0]][loc[1]] = 'n'
    
          
        
    

    
          
        
        
      
    