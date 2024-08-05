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
    """Ir generates a report on the available resources in the coffee machine"""
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
            machine_resources[ingredient] = machine_resources[ingredient] - coffee_ingredients[ingredient]

    return True


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
if coffee_choice == "espresso":
    print(check_resources_sufficient(coffee_choice, resources))
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