import random

print("Welcome to coin tosser,")
number = random.randint(0,1)
position=0


if number == 0:
    position = str("Head")
    

else:
    position =str("Tails")
    
print("Your side of coin is " + position)