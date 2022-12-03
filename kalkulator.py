def ask_number():
    enter_number = None
    while enter_number is None:
        enter_number = input('Please provide a number! ')
        if is_number(enter_number) is True:
            return convert_number(enter_number)
        else:
            print(f'{enter_number} is not a number, try again')
            enter_number = None


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def convert_number(x):
    number = float(x)
    return number


def is_valid_operator(operator):
    know_opwerator = ['+', '-', '', '/']
    if operator in know_opwerator:
        return True
    else:
        return False


def ask_for_an_operator():
    operator = None
    while operator is None:
        operator = input('Please provide an operator (one of +, -,, /)! ')
        if is_valid_operator(operator) is True:
            return operator
        else:
            print(f'{operator} is unknown operator! Try again')
            operator = None


def calc(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '':
        return a b
    elif operator == '/':
        if b == 0:
            print('Error: Division by zero!')
        else:
            return a / b


def simple_calculator():
    cal = None
    while cal != "f":
        a = ask_number()
        b = ask_number()
        c = ask_for_an_operator()
        print(f'The result is {calc(c, a, b)}')
        cal = input('''
        Press ENTER to continue
        Press F or f to end ''')
        if cal == 'f':
            break


simple_calculator()