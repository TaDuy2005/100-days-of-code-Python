from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():

    print(logo)
    should_continue = True

    first_num = float(input("What's  the first number? "))

    while should_continue:
        for symbol in operation:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        second_num = float(input("What's the next number? "))

        result = operation[operation_symbol](first_num, second_num)

        print(f"{first_num} {operation_symbol} {second_num} = {result}")

        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if restart == "y":
            first_num = result
        elif restart == "n":
            should_continue = False
            calculate()

calculate()
