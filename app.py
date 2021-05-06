from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from moneymachine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("Machine turned off.")
        is_on = False
    else:
        try:
            drink = menu.find_drink(user_choice)
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            if is_enough_ingredients:
                is_payment_successful = money_machine.make_payment(drink.cost)
                if is_payment_successful:
                    coffee_maker.make_coffee(drink)
        except AttributeError:
            print("Sorry that item is not available.")
    print()

