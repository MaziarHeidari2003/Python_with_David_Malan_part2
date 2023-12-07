import sys

if len(sys.argv) > 2 :
  sys.exit("Too many arguements")
elif len(sys.argv) < 2 :
  sys.exit("Too few arguements")

print("hello , my name is", sys.argv[1])