from objects.menu import Menu
from objects.coffee_maker import CoffeeMaker
from objects.money import MoneyMachine


def main(menu, coffee, money):
    decision = input(f"What would you like? {menu.get_items()} ")
    
    if decision == 'latte':
        print("decision: latte")
        make_drink(menu.find_drink(decision), coffee, money)
    elif decision == 'cappuccino':
        make_drink(menu.find_drink(decision), coffee, money)
    elif decision == 'espresso':
        make_drink(menu.find_drink(decision), coffee, money)
    elif decision == 'off':
        return False     
    elif decision == 'report':
        coffee.report()
        money.report()      
    return True

def make_drink(menu, coffee, money):
    if coffee.is_resource_sufficient(menu):
        print(f"Preparing your order.\nTotal: ${menu.cost}.")
        payment = money.make_payment(menu.cost)
        if payment:
            coffee.make_coffee(menu)

if __name__ == "__main__":
    menu_obj = Menu()
    coffee_maker_obj = CoffeeMaker()
    money_machine_obj = MoneyMachine()

    next_customer = True

    while next_customer:
        next_customer = main(menu_obj, coffee_maker_obj, money_machine_obj)
        if next_customer == False:
            print("Good-bye")
            exit(1)