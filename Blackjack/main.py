cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

import os

def clear():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

computer_card=[]
user_card=[]

def cards_in_beggining(edited_list,list):
    for cards in range(2):
        edited_list.append(random.choice(list))
    return edited_list


user_sum=0
computer_sum=0
def calculate_score(list):
    return sum(list)

def add_new_card(new_list,card):
    new_list.append(random.choice((card)))
    return new_list


start=True
while start:
    computer_card=cards_in_beggining(edited_list=computer_card,list=cards)
    user_card=cards_in_beggining(edited_list=user_card,list=cards)
    computer_sum=calculate_score(computer_card)
    user_sum=calculate_score(user_card)

    print(f"Your cards are {user_card}")
    print(f"Computer's first card is {computer_card[0]}")

    condition=True
    while condition:
        add=input("Do you want to add a new card? yes if u want to hold no.").lower()
        if add == "yes":
            user_card=add_new_card(user_card,cards)
            print(f"Your new cards are {user_card}")
            user_sum=calculate_score(user_card)
            if user_sum > 21:
                if 11 in user_card:
                    user_card.remove(11)
                    user_card.append(1)
                else:
                    print("You ran over,, game over soorry......")
               
                    condition=False

                
        elif add== "no":
            condition = False
    user_sum=calculate_score(user_card)
    computer_sum=calculate_score(computer_card)
    if user_sum>computer_sum and user_sum<21:
        print("You win!!!!!!!!!!!!!!!!!")
    elif user_sum == 21:
        print("you win")
    else:
        print("you lost")
            
    new_game=i=input("Do you wana retry yes or no?")
    if new_game == "no":
        start=False
    else:
        clear()
        user_card=[]
        computer_card=[]
         