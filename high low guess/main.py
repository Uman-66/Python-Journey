from art import logo,vs
from data import data
import random
import os

def clear():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

score=0

no1=random.choice(data)

no2=random.choice(data)


start=True
while start:
    no1=random.choice(data)

    no2=random.choice(data)
    print(logo)
    print(f"Your current score is {score}")
    print(f"Compare A: {no1["name"]},{no1["description"]} from {no1["country"]}")
    print(vs)
    print(f"Compare B: {no2["name"]},{no2["description"]} from {no2["country"]}")
    choice=input("You have to choose A or B, Which of these have higher followers on instagram").lower()
    if choice=="a" and no1["follower_count"]>no2["follower_count"]:
        score= score+1
        print("you win")
        clear()
    elif choice=="b" and no2["follower_count"]>no1["follower_count"]:
        score= score+1
        print("you win")
        clear()
    else:
        start=False
        clear()
print(f"Your score is {score} and u lost")