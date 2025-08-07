from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_true=True

while is_true:
    option=menu.get_items()
    choice=input(f"Would you like to make {option} or report ")
    if choice == "off":
        is_true=False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            # money_machine.process_coins()