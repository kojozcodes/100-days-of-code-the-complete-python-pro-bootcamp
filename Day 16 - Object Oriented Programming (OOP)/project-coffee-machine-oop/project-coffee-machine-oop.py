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

    if choice == espresso.name or choice == latte.name or choice == cappuccino.name:
        print(choice)
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "off":
        print("Goodbye!")
        is_on = False