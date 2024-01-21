from modules import coffee_machine_printing
from modules import coffee_machine_maths
from data import coffee_recipie


def check_resources(user_choice):
    water = coffee_recipie.MENU[user_choice]['ingredients']['water']
    coffee = coffee_recipie.MENU[user_choice]['ingredients']['coffee']

    remaining_water = coffee_recipie.resources['water']
    remaining_coffee = coffee_recipie.resources['coffee']
    
    if user_choice == 'latte' or user_choice == 'cappuccino':
        milk = coffee_recipie.MENU[user_choice]['ingredients']['milk']
        remaining_milk = coffee_recipie.resources['milk']
        if remaining_milk < milk:
            coffee_machine_printing.print_insufficient_resources('milk')
            return 1
    
    if remaining_water < water:
        coffee_machine_printing.print_insufficient_resources('water')
        return 1
    elif remaining_coffee < coffee:
        coffee_machine_printing.print_insufficient_resources('coffee')
        return 1
   
    else: 
        coffee_machine_maths.remove_resources(user_choice)


def options(user_choice):
    if user_choice == 'off':
        coffee_machine_printing.print_power_off()
        exit(1)
    elif user_choice == 'report':
        coffee_machine_printing.print_report()
        return 1
    elif user_choice == 'espresso' or user_choice== 'latte' or user_choice == 'cappuccino':
        if check_resources(user_choice) == 1:
            return 1
        else:
            return 0
    return 1


def main():
    next_drink = True

    while next_drink:
        choice = input("What would you like to drink? (espresso/latte/cappuccino) ").lower()
        if options(choice) == 1:
            continue
        else:
            
            provided_total = coffee_machine_maths.accept_coins()
            if  provided_total < coffee_recipie.MENU[choice]['cost']:
                coffee_machine_printing.print_refund()
            else:
                coffee_machine_printing.print_change(coffee_machine_maths.provide_change(coffee_recipie.MENU[choice]['cost'], provided_total))
                coffee_machine_printing.print_drink(choice)


if __name__ == '__main__':
    main()