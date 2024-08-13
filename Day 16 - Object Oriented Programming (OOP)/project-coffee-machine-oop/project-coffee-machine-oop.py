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
    else:
        coffee_menu_dictionary = coffee_menu.menu
        for coffee_type in range(len(coffee_menu_dictionary)):
            if choice == coffee_menu_dictionary[coffee_type].name:

                if coffee_maker.is_resource_sufficient(coffee_menu_dictionary[coffee_type]):

                    if money_machine.make_payment(coffee_menu_dictionary[coffee_type].cost):
                        coffee_maker.make_coffee(coffee_menu_dictionary[coffee_type])