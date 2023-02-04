# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO:2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.


# TODO:3. Print report
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5



# TODO:4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

money=0.0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water:{resources['water']}")
    print(f"Milk:{resources['milk']}")
    print(f"Coffee:{resources['coffee']}")
    print(f"Money:{money}")

def check_resources(coffee_type):
    for item in coffee_type:
        if coffee_type[item]>resources[item]:
            print(f'there is not enough {item}')
            return False
        return True

def process_coins():
    print("Please Enter Coins!!!")
    total=int(input("Enter the number of quarters:"))*0.25
    total+=int(input("Enter the number of dimes:"))*0.1
    total+=int(input("Enter the number of nickels:"))*0.05
    total+=int(input("Enter the number of penny:"))*0.01
    return total

def transaction_success(total, drink_cost):
    if total<drink_cost:
        print("Not enough money")
        print(f"Returned amount:{total}")
        return False
    else:
        global money
        money+=drink_cost
        print(f"Returned amount:{round(total-drink_cost,2)}")
        return True

def make_drink(drink, ingridients):
    for item in ingridients:
        resources[item]-=ingridients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")



power_on=True
while power_on:
    user_choice=input("What would you like? (espresso/latte/cappuccino):")
    if user_choice=="off":
        power_on=False
    elif user_choice=="report":
        report()
    else:
        if check_resources(MENU[user_choice]["ingredients"]):
            total=process_coins()
            if transaction_success(total, MENU[user_choice]["cost"]):
                make_drink(user_choice, MENU[user_choice]["ingredients"])
