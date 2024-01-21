from data import coffee_recipie

def print_report():
    print(f"Water: {coffee_recipie.resources['water']}ml")
    print(f"Milk: {coffee_recipie.resources['milk']}ml")
    print(f"Coffee: {coffee_recipie.resources['coffee']}ml")
    print(f"Money: ${coffee_recipie.resources['money']}")

def print_power_off():
    print("Powering off machine... Good-bye!")

def print_change(change):
    print(f"Here is your ${change:.2f} in change.")

def print_insufficient_resources(resource):
    print(f"Sorry, there is not enough {resource}.")


def print_drink(drink):
    print(f"Here is your {drink:.2f}. Enjoy!")

def print_refund():
    print(f"Sorry, that's not enough money. Money refunded.")