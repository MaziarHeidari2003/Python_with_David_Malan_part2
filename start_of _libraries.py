"""
import random

coin = random.choice(["heads","tails"])
print(coin)
"""
"""
from random import choice

coin = choice(["heads","tails"])
print(coin)
"""
"""

import random
number = random.randint(1,100)
print(number)
"""
"""

import random 
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
  print(card)
"""
"""
import statistics
print(statistics.mean([100,100,80,60]))
"""

import sys
print("hello my name is", sys.argv[1])

