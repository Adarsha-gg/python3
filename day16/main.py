from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resource = CoffeeMaker()
menu = Menu()
is_on = True
money = MoneyMachine()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":    
        resource.report()
        money.report()
    else:
        cofi = menu.find_drink(choice)
        if resource.is_resource_sufficient(cofi) and money.make_payment(cofi.cost):
            resource.make_coffee(cofi)