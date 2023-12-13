"""
Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random

def main():
  level = get_level()
  score = simulate_game(level)
  print(f'score: {score}')



def get_level() :
  while True:
    try:
      level = int(input('Level: '))
      if level in [1,2,3] :
        return level
    except:
      pass    


def generate_integer(level):
  if level == 1 :
    x = random.randint(0,9)
    y = random.randint(0,9)
  if level == 2 :
    x = random.randint(10,99)
    y = random.randint(10,99)
  if level == 3 :
    x = random.randint(100,999)
    y = random.randint(100,999)   
  return x,y


def simulate_round(x,y):
  cnt = 1
  while cnt <= 3 :
    try:
      answer = int(input(f'{x} + {y} = '))
      if answer == x + y :
        return True
      else:
        print('EEE')  
        cnt += 1
    except ValueError:
      cnt += 1
      print('EEE')
  print(f'{x} + {y} = {x+y}')
  return False


def simulate_game(level) :
  score = 0
  for i in range(10) :
    x,y = generate_integer(level)
    response = simulate_round(x,y)
    if response == True:
      score += 1
  return score
      

if __name__ == '__main__' :
  main()