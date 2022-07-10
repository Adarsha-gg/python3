MENU = {
    "espresso": {
        "ingredients": {
            "water": 500,
            "coffee": 18,
            "milk":0
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
    "water": 00,
    "milk": 200,
    "coffee": 100,
    "money":0
}
yn= True
def report():
        print(f"Milk: {resources['milk']}ml\n Water: {resources['water']}ml\n Milk: {resources['coffee']}gm\n")

def sufficient():
    if(resources['milk'] >= MENU[choice]["ingredients"]['milk']):
        resources['milk'] - MENU[choice]["ingredients"]['milk']
    elif resources['milk'] < MENU[choice]["ingredients"]['milk']:
        print("Sorry there is not enough milk")

    if(resources['coffee'] >= MENU[choice]["ingredients"]['coffee']):
       resources['coffee'] - MENU[choice]["ingredients"]['coffee']
    else:
        print("Sorry there is not enough milk")

    if(resources['water'] >= MENU[choice]["ingredients"]['water']):
       resources['water'] >= MENU[choice]["ingredients"]['water']
    else:
        print("Sorry there is not enough milk")

def costt(choice):
    if(choice == "espresso"):
        return MENU["espresso"]["cost"]
    elif(choice == "latte"):
        return MENU["latte"]["cost"]
    elif(choice == "cappuccino"):
        return MENU["cappuccino"]['cost']

def drink():
    if(choice == "espresso"):
        if(sufficient() == True) :
            print("Here is your espresso")
    elif(choice == "latte"):
        if(sufficient() == True) :
            print("Here is your latte")
    elif(choice == "cappuccino"):
        if(sufficient() == True) :
            print("Here is your cappuccino")

def coins(price):
    quat = int(input("How many quaters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.05
    nickels = int(input("How many nickels?")) *0.10
    pennies = int(input("How many pennies?")) * 0.01
    total = quat + dimes + nickels + pennies
    if (total >= price):
        change = total - price
        print(f"Here is your ${change}")
        drink()
    elif(total < price):
        print ("Not enough coins")
        return 0

while yn == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if (choice == "report"):
        report(choice)
    else:
        price_g = costt(choice)
        coins(price_g)            
    if input("Would u like another drink: ").lower() == "y":
        yn = True
    else:
        yn = False    