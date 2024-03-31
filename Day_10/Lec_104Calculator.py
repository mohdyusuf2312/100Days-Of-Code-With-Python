import os
import art as l

print(l.logo_Calculator)
def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        _ = os.system('clear')

# add
def add(n1, n2):
    return n1 + n2

#sub
def sub(n1, n2):
    return n1 - n2

#mul
def mul(n1, n2):
    return n1 * n2

#div
def div(n1, n2):
    if n2 == 0:
        print("Denominator can't be zero.")
        return
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    n1 = float(input("Enter first number: "))
    for n in operation:
        print(n)

    loop = True
    while loop == True:
        op = input("Enter operation: ")
        n2 = float(input("Enter next number: "))
        function = operation[op]
        result = function(n1, n2)
        print(f"Do you want to more calculation with {result}? ")
        more = input("Type 'y' for yes, type 'n' for new calculation and type 'e' for exit: ").lower()
        if more == "y":
            n1 = result
        elif more == "n":
            clear_console()
            calculator()
        elif more == "e":
            loop = False

calculator()