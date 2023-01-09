# name: Ali Thursland
# date: 2019-11-17
# title: Text-based RPG

from player import Player

def play():
  print("Escape from Cave Terror!")
  player = Player()
  while True:
      if action_input in ['n','N']:
          print("Go North!")
      elif action_input in ['s','S']:
          print("Go South!")
      elif action_input in ['e', 'E']:
        print("Go East!")
      elif action_input in ['w', 'W']:
        print("Go West!")
      elif action_input in ['i', 'I']:
        player.print_inventory()
      else:
        print("Invalid action!")


def get_player_comand():
    return input('Action: ')


play()
