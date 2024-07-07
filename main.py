from sys import exit
from functions import calc_coins

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
is_on=True
while is_on:
    # TODO: 1. Get input from user(report, coffee type, off,...)
    user_choice = (input("What would you like? (espresso/latte/cappuccino):").lower())

    # TODO: 2. Actions outside of ordering(report, off)
    if user_choice == "report":
        for ingredient, value in resources.items():
            print(ingredient, ":", value)
    elif user_choice == "off":
        is_on = False
        exit(0)

    # TODO: 3.check resources when ordering

    elif user_choice in MENU:
        enough_resources = True
        enough_money = True
        for ingredient in MENU[user_choice]["ingredients"]:
            available_ingredient_amount = resources[ingredient]
            needed_ingredient_amount = MENU[user_choice]["ingredients"][ingredient]
            # print(available_ingredient_amount)
            # print(needed_ingredient_amount)
            if available_ingredient_amount < needed_ingredient_amount:
                enough_resources = False
                print(f"Sorry, there is not enough {ingredient}")
        # TODO: 4. Process coins
        if enough_resources:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_amount = calc_coins(quarters, dimes, nickels, pennies)

            # TODO: 5. Check transaction

            if total_amount < MENU[user_choice]["cost"]:
                enough_money = False
                print("Sorry, that's not enough money. Money refunded.")
            elif total_amount >= MENU[user_choice]["cost"]:
                profit += MENU[user_choice]["cost"]
                resources.update(({"Money": profit}))
                if total_amount > MENU[user_choice]["cost"]:
                    change = total_amount - MENU[user_choice]["cost"]
                    print(f"Here is {change:.2f} in change.")

        # TODO: 6. Deduct resources
        if enough_resources and enough_money:
            for deduction in MENU[user_choice]["ingredients"]:
                resources[deduction] -= MENU[user_choice]["ingredients"][deduction]
            print(f"Here is your {user_choice}. Enjoy!")
