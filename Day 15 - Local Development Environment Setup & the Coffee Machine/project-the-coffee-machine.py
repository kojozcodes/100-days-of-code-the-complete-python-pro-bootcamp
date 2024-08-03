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

# TODO 3: Print report.


def report():
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource}: {resources[resource]}g")
        else:
            print((f"{resource}: ${resources[resource]}"))
# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


is_on = True

while is_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino: ").lower()
    if user_choice == "espresso":
        print("espresso")
    elif user_choice == "latte":
        print("latte")
    elif user_choice == "cappuccino":
        print("cappuccino")
    elif user_choice == "report":
        report()

# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    elif user_choice == "off":
        is_on = False

# TODO 4: Check resources sufficient?


# TODO 5: Process coins.


# TODO 6: Check transaction successful?


# TODO 7: Make Coffee.
print("hello")
