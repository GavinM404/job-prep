def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1/number2


def multiply(number1, number2):
    return number1 * number2


def calc():
    yes = True

    while yes == True:
        print('Welcome to my calculator!')
        number1 = int(input('What is your first number?'))
        number2 = int(input('What is your second number?'))
        operation = input('What operation would you like to do? + - / * ')

        if operation == '+':
            print(add(number1, number2))
        elif operation == '-':
            print(subtract(number1, number2))
        elif operation == '/':
            print(divide(number1, number2))
        elif operation == '*':
            print(multiply(number1, number2))

        cont = input('Would you like to go again? Yes/No').lower()

        if cont == 'yes':
            yes = True
        else:
            yes = False

calc()
