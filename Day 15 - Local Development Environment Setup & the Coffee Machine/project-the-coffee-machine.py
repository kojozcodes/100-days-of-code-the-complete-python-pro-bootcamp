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
        if resource == "water" or resource == "milk":
            print(f"{resource.title()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.title()}: {resources[resource]}g")
        elif resource == "money":
            print(f"{resource.title()}: ${resources[resource]}")


def check_resources_sufficient(coffee, machine_resources):
    coffee_ingredients = MENU[coffee]["ingredients"]
    for ingredient in MENU[coffee]["ingredients"]:
        for resource in machine_resources:
            if ingredient in machine_resources and ingredient == resource:
                if machine_resources[resource] >= coffee_ingredients[ingredient]:
                    print(True)
                else:
                    print(False)


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
if coffee_choice == "espresso":
    check_resources_sufficient(coffee_choice, resources)
elif coffee_choice == "latte":
    check_resources_sufficient(coffee_choice, resources)
elif coffee_choice == "cappuccino":
    check_resources_sufficient(coffee_choice, resources)

# TODO: 3. Print report.
elif coffee_choice == "report":
    generate_report()

# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt
elif coffee_choice == "off":
    print("off")

# for ingredient in MENU["latte"]["ingredients"]:
#     for resource in resources:
#         if ingredient in resources and ingredient == resource:
#             calc = resources[resource] - MENU["latte"]["ingredients"][ingredient]
#             resources[resource] = calc
#             print(calc)

generate_report()
