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
    "water": 200,
    "milk": 200,
    "coffee": 100,
    "money":0
}
yn= True
def report():
        print(f"Milk: {resources['milk']}ml\n Water: {resources['water']}ml\n Milk: {resources['coffee']}gm\n")

def sufficient():
    milk =MENU[choice]["ingredients"]['milk']
    coffee = MENU[choice]["ingredients"]['coffee']
    water = MENU[choice]["ingredients"]['water']
    if(resources['milk'] >= milk):
        resources['milk'] -= milk
        return True
    else:
        print("Sorry there is not enough milk")
        return False

    if resources['coffee'] >= coffee:
       resources['coffee'] -= coffee
       return True
    else:
        print("Sorry there is not enough coffee")
        return False

    if(resources['water'] >= water):
       resources['water'] -= water
       return True
    else:
        print("Sorry there is not enough water")
        return False

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
    print("PLEASE ENTER COINS \n")
    quat = int(input("How many quarters?")) * 0.25
    nickels = int(input("How many nickels?")) *0.10
    dimes = int(input("How many dimes?")) * 0.05
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
        report()
        use = input("Would u like a drink: (y/n)").lower()    
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        price_g = costt(choice)
        coins(price_g)  
        use = input("Would u like another drink: (y/n)").lower()      
    else:
        print("Enter a valid command")    
            
    if  use == "y":
        yn = True
    elif use == "n":
        print("Thanks for using our machine")
        yn = False
    else:
        print("Please enter a valid command")        