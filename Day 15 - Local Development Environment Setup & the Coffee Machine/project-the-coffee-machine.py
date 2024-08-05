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
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
if coffee_choice == "espresso":
    print("espresso")
elif coffee_choice == "latte":
    print("latte")
elif coffee_choice == "cappuccino":
    print("cappuccino")

# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt
elif coffee_choice == "off":
    print("off")

# TODO: 3. Print report.
elif coffee_choice == "report":
    generate_report()