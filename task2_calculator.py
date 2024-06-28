def add(u,v):
    return u + v

def subtract(u, v):
    return u - v

def multiply(u,v):
    return u * v

def divide(u,v):
    if v != 0:
        return u / v
    else:
        return "Error! Division by zero."

def expo(u,v):
    return u ** v

def modulus(u,v):
    if v != 0:
        return u % v
    else:
        return "Error! Modulus by zero."

def floor_divide(u,v):
    if v != 0:
        return u // v
    else:
        return "Error! Floor division by zero."

def calculator():
    print("Enter the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Floor Divide")

    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} ^ {num2} = {expo(num1, num2)}")

        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice == '7':
            print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
    else:
        print("Invalid input")

calculator()
 