"""
Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random

while True:
  try:
    level = int(input('Level: '))
    if level >= 1 :
      break
  except ValueError:
    pass  

com_guess = random.choice(range(1,level+1))

while True:
  try:
    play_guess = int(input('Guess: '))
    if play_guess >= 1 and play_guess == com_guess :
      print('Just right')
      break
    elif play_guess > com_guess :
      print('Too large')
    else :
      print('Too small')  
  except ValueError:
    pass  

