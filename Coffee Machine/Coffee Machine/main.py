from functools import total_ordering
from timeit import default_timer
from turtledemo.penrose import start

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def show_report(quantity):
    print(f'water : {quantity["water"]}')
    print(f'milk : {quantity["milk"]}')
    print(f'coffee : {quantity["coffee"]}')

def check_resources(required,left,sources):
    if sources[required]["ingredients"]["water"]> left["water"]:
        print("Sorry, you don't have enough water")


    if sources[required]["ingredients"]["milk"]> left["milk"]:
        print("Sorry, you don't have enough milk")

    if sources[required]["ingredients"]["coffee"] > left["coffee"]:
        print("Sorry, you don't have enough coffee")


def deduction(source,used,order):
    source["water"] = source["water"] - used[order]["ingredients"]["water"]
    source["milk"] = source["milk"] - used[order]["ingredients"]["milk"]
    source["coffee"] = source["coffee"] - used[order]["ingredients"]["coffee"]

def enter_money():
    print("Insert your coins here")
    penny=float(input("Penny:"))
    dime=float(input("Dime:"))
    nickle=float(input("Nicks:"))
    quarter=float(input("Quarters:"))
    total=0
    total+=penny*0.01
    total+=dime*0.10
    total+=nickle*0.05
    total+=quarter*0.25
    return total

earned=0.0
machine=True
while machine:

    item=input("What would you like? cappuccino,latte or espresso or you want a report?").lower()

    if item == "report":
        show_report(resources)
        print(earned)


    elif item in ["espresso", "latte", "cappuccino"]:
        if MENU[item]["ingredients"]["water"] > resources["water"] or MENU[item]["ingredients"]["water"] > resources["water"] or MENU[item]["ingredients"]["water"] > resources["water"]:
            check_resources(required=item,left=resources,sources=MENU)


        else:
            money=enter_money()
            if money < MENU[item]["cost"]:
                print("Sorry, you don't have enough money,take it back")

            elif money >= MENU[item]["cost"]:
                print(f"Here, your {item}")
                earned += MENU[item]["cost"]
                change=money-MENU[item]["cost"]
                print(f"Your change is {change}")
                deduction(source=resources, used=MENU, order=item)
