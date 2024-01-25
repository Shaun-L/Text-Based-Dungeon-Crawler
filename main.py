#Shaun Lim and Daniel Hernandez
#The same as our last lab, this program allows the user to wander through a dungeon maze and fight monsters that they encounter as they explore. The main difference with this lab is new dungeon maps will load once the user makes it to the end of their map. This is done using a singleton map class as well as different entity objects and factories creating those objects. (All menu inputs are checked using check_input)

import map
import hero
import check_input
import random
import beg_factory
import exp_factory

def main():
  """the function that takes in user inputs, and runs the game accordingly."""

  #creating the the inital variables after asking the user for their name.
  user_name = input("What is your name, traveler? ")

  user = hero.Hero(user_name, 25)
  game_map = map.Map()
  current_map = 1

  difficulty = check_input.get_int_range("Difficulty:\n1.Beginner\n2.Expert\n", 1, 2)

  user_input = 0

  #The main while loop that keeps running until the player dies or when the user chooses to quit.
  while (user.hp != 0) and (user_input != 5):

    #printing the user name, hp, game map, and list of options.
    print(user)
    game_map.show_map(user.loc)
    user_input = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: ", 1, 5)


    #if statements that respond accordingly to user input, revealing their previous location as well as moving their current location and storing it in the room variable
    if user_input == 1:
      game_map.reveal(user.loc)
      room = user.go_north()
    elif user_input == 2:
      game_map.reveal(user.loc)
      room = user.go_south()
    elif user_input == 3:
      game_map.reveal(user.loc)
      room = user.go_east()
    elif user_input == 4:
      game_map.reveal(user.loc)
      room = user.go_west()
    else:
      break


    
    if room == 'x':
      #Check to see if the user is out of bounds.
      print('You cannot go that way...')
      
    elif game_map[room[0]][room[1]] == 'm':
      #This is the monster room. Here we create the enemy object using the correct factory depending on what difficulty that the user has chosen initially.
      game_map.reveal(user.loc)
      if difficulty == 1:
        monster = beg_factory.BeginnerFactory().create_random_enemy()
      else:
        monster = exp_factory.ExpertFactory().create_random_enemy()
        
      print("You encounter a "+str(monster))

      #After printing the health and monster encounter, this while loop presents another list of options, running away or attacking. This runs until the monster dies or the user dies. The loop also breaks when the user runs away.
      while monster.hp != 0 and user.hp != 0:
        choice = check_input.get_int_range(f"1. Attack {monster.name}\n2. Run Away\nEnter choice: ",1,2)
        
        if choice == 1:
          #When choosing to attack, the user attacks first and if the monster survives, it attacks the user.
          print(user.attack(monster))
          if monster.hp != 0:
            print(monster.attack(user))
            
        else:
          #if the user selects to run random direction is chosen to run away
          print("You ran away!")
          rand_loc = 'x'
          while rand_loc == 'x':
            #In case the random location turns up to be out of bounds, this while loop keeps running until the location ran to is in bounds.
            rand = random.randint(1,4)
            if rand == 1:
              rand_loc = user.go_north()
              game_map.reveal(user.loc)
            elif rand == 2:
              rand_loc = user.go_south()
              game_map.reveal(user.loc)
            elif rand == 3:
              rand_loc = user.go_east()
              game_map.reveal(user.loc)
            else:
              rand_loc = user.go_west()
              game_map.reveal(user.loc)
          break
          
      if monster.hp == 0:
        #When the monster is defeaten, there will no longer be a monster at the location
        game_map.remove_at_loc(user.loc)
          
    elif game_map[room[0]][room[1]] == 'n':
      #This represnts a room with nothing in it
      print('There is nothing here...')
      
    elif game_map[room[0]][room[1]] == 's':
      #This represents the room where the user started at
      print('You are back at the start of the dungeon...')
      
    elif game_map[room[0]][room[1]] == 'i':
      #This room a the room with a health potion that heals the user to full health once.
      print('You found a Health Potion! You drink it to restore your health.')
      user.heal()
      game_map.remove_at_loc(user.loc)
      
    elif game_map[room[0]][room[1]] == 'f':
      #This is the final location, when the user arrives here, we increment the current map variable and load the next map while checking to make sure it will only load maps 1, 2, and 3
      print('Congratulations! You found the stairs to the next floor of the dungeon.')
      if (current_map+1) == 4:
        current_map = 0
      current_map += 1
      game_map.load_map(current_map)
      

  if user.hp == 0:
    #If the while loop is broken when the user dies, this is an extra statement showing the user they have died.
    print("You died...")
    
  print("Game Over")

    
      



main()
