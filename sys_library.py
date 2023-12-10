import sys
"""
if len(sys.argv) < 2 :
  #print("Few arguements")
    sys.exit("Few arguements")

elif len(sys.argv) > 2 :
  #print("Too many arguements")
    sys.exit("Too many arguements")

else :
  print("hello, your name is", sys.argv[1])    
  """

if len(sys.argv) < 2 :
    sys.exit("Few arguements")

for arg in sys.argv[1:]:
    print("hello my name is", arg)    
