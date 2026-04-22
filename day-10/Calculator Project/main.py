import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    # Cálculo inicial
    print(art.logo)
    n1 = float(input("What is your first number?: \n"))
    operator = input("What operation would you like to perform? '+', '-', '*', '/': \n")
    n2 = float(input("What is your second number?: \n"))
    result = operations[operator](n1, n2)
    print(n1, operator, n2, "=", result)

    # Loop de continuação com o resultado anterior
    while True:
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: \n")
        if choice == "y":
            operator = input("What operation would you like to perform? '+', '-', '*', '/': \n")
            n2 = float(input("What is your next number?: \n"))
            previous_result = result
            result = operations[operator](result, n2)  # result vira o novo n1
            print(previous_result, operator, n2, "=", result)
        elif choice == "n":
            print("\n" * 100)
            break
        else:
            break  # sai do loop interno, o externo reinicia tudo