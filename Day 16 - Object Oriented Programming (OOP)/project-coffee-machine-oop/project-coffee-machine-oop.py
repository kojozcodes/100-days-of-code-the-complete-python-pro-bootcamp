from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

espresso = coffee_menu.find_drink("espresso")
latte = coffee_menu.find_drink("latte")
cappuccino = coffee_menu.find_drink("cappuccino")

is_on = True

while is_on:
    choice = input(f"What would you like to order? ({coffee_menu.get_items()}): ").lower()

    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        for coffee_index in range(len(coffee_menu.menu)):
            coffee_type = coffee_menu.menu[coffee_index]
            if choice == coffee_type.name:
                if coffee_machine.is_resource_sufficient(coffee_type):
                    print(f"can make {coffee_type.name}")