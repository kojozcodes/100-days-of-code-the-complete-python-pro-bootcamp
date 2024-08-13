from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like to order? ({coffee_menu.get_items()}): ").lower()

    if choice == "off":
        print("Goodbye!")
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == coffee_menu.find_drink(choice).name:

        coffee_drink = coffee_menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(coffee_drink):

            if money_machine.make_payment(coffee_drink.cost):
                coffee_maker.make_coffee(coffee_drink)