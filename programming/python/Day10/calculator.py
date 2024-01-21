from modules import calculator_art

def logo():
    print(calculator_art.logo)

def operators():
    print("+\n-\n*\n\\")

def calculate(num1, op, num2):
    '''
        Alternatively you can do:
        operations = {
            "+": +,
            "-": -,
            "*": *,
            "/": /,
        }
        operator = operations[op] 
    '''
    expression = num1 + op + num2
    return eval(expression)
#Recursion
def clear_calculator():
    return input("What's the first number?: ")


if __name__ == "__main__":
    logo()
    next_calculation = True
    number1 = clear_calculator()
    
    while next_calculation == True:
        
        operators()
        operator = input("Pick an operation: ")
        number2 = input("What's the next number?: ")
        result = calculate(num1=number1, num2=number2, op=operator)
        print(f"{number1} {operator} {number2} = {result}")
        answer = input("Type 'y' to continue calculating with the answer.\nType 'c' to clear and perform new calculations.\nType 'n' to exit.\n").lower()
        if answer == 'y':
            number1 = str(result)
        elif answer == 'c':
            number1 = clear_calculator()
        else: 
            next_calculation = False



