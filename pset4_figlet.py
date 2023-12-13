import sys
import random
from pyfiglet import Figlet

figlet = Figlet()



if len(sys.argv) == 1 :
  random_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] =='--font') :
  random_font = False
else: 
  sys.exit('Invalid usage')  


if random_font == False :
  try:
    figlet.setFont(font=sys.argv[2])
  except:
    sys.exit('Invalid usage2')  
else:
  random.choice(figlet.getFonts()) 

msg = input('Input: ')

print('Output: ')
print(figlet.renderText(msg))


