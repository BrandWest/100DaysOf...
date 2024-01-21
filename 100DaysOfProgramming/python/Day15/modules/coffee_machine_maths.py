from data import coffee_recipie

def provide_change(cost, money):
    return money - cost


def get_totals(quarters, dimes, nickles, pennies):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.1
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01

    return total_quarters + total_dimes + total_nickles + total_pennies


def accept_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    return get_totals(quarters, dimes, nickles, pennies)

def remove_resources(user_choice):
    water = coffee_recipie.MENU[user_choice]['ingredients']['water']
    coffee = coffee_recipie.MENU[user_choice]['ingredients']['coffee']
    remaining_water = coffee_recipie.resources['water']
    remaining_coffee = coffee_recipie.resources['coffee']
        
    if user_choice == 'latte' or user_choice == 'cappuccino':
        milk = coffee_recipie.MENU[user_choice]['ingredients']['milk']
        remaining_milk = coffee_recipie.resources['milk']
        remaining_milk -= milk
        coffee_recipie.resources['milk'] = remaining_milk

    remaining_water -= water
    remaining_coffee -= coffee
    coffee_recipie.resources['water'] = remaining_water
    coffee_recipie.resources['coffee'] = remaining_coffee

    coffee_recipie.resources['money'] += coffee_recipie.MENU[user_choice]['cost']