from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

espresso = coffee_menu.find_drink("espresso")
latte = coffee_menu.find_drink("latte")
cappuccino = coffee_menu.find_drink("cappuccino")
