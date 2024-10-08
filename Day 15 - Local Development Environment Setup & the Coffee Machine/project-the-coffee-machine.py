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


def generate_report():
    """It generates a report on the available resources in the coffee machine"""
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource.title()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.title()}: {resources[resource]}g")
        elif resource == "money":
            print(f"{resource.title()}: ${resources[resource]}")


def check_resources_sufficient(coffee, machine_resources):
    """
        It takes the coffee type the user wants and the available resources in the machine,
        to determine if the machine can produce the coffee
    """
    coffee_ingredients = MENU[coffee]["ingredients"]

    for ingredient in coffee_ingredients:
        if ingredient in machine_resources:
            if machine_resources[ingredient] < coffee_ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
    return True


def process_coins(quarter, dime, nickel, penny):
    """It takes four different coins, converts them to dollars and add them up together"""
    return (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)


def check_transaction_successful(coffee, coins):
    """It takes the choice of coffee of the user and the money they put.
        It checks if the total money put in the machine meets the cost of making the coffee
    """
    coffee_price = MENU[coffee]["cost"]
    if coins < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if coins > coffee_price:
        change = "{:.2f}".format(coins - coffee_price)
        print(f"Here is ${change} dollars in change")
    return True


is_on = True
profit = 0

while is_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        if check_resources_sufficient(coffee_choice, resources):

            print("Please insert coins.")

            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many quarters?: "))
            total_coins = process_coins(quarters, dimes, nickles, pennies)

            if check_transaction_successful(coffee_choice, total_coins):
                for coffee_ingredient in MENU[coffee_choice]["ingredients"]:
                    if coffee_ingredient in resources:
                        resources[coffee_ingredient] -= MENU[coffee_choice]["ingredients"][coffee_ingredient]
                profit += MENU[coffee_choice]["cost"]
                resources["money"] = profit
                print(f"Here is your {coffee_choice}. Enjoy!")

    elif coffee_choice == "report":
        generate_report()

    elif coffee_choice == "off":
        print("Goodbye!")
        is_on = False

# for ingredient in MENU["latte"]["ingredients"]:
#     for resource in resources:
#         if ingredient in resources and ingredient == resource:
#             calc = resources[resource] - MENU["latte"]["ingredients"][ingredient]
#             resources[resource] = calc
#             print(calc)

