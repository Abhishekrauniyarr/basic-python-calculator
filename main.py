
# function

def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    sub = a - b
    return sub

def mul(a, b):
    multiply = a * b
    return multiply

def div(a, b):
    if b == 0:
        return "Undefined (cannot divide by zero)"
    div = a / b
    return div


# Calculator

while True:

    print("\n          PYTHON CALCULATOR\n")

    print("Available Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("\nSelect an operation (1-5): "))

        if choice == 5:
            print("\nThank you for using Python Calculator.")
            print("Program closed successfully.")
            break

        elif choice not in (1, 2, 3, 4):
            print("\nInvalid choice. Please select a valid operation.")
            continue

        print("\nEnter the numbers")

        a = float(input("First number: "))
        b = float(input("Second number: "))

    except ValueError:
        print("\nInvalid input. Please enter numeric values.")
        continue

    if choice == 1:
        result = add(a, b)
        operation = "Addition"

    elif choice == 2:
        result = sub(a, b)
        operation = "Subtraction"

    elif choice == 3:
        result = mul(a, b)
        operation = "Multiplication"

    elif choice == 4:
        result = div(a, b)
        operation = "Division"

    print("\nCalculation Result")
    print(f"Operation: {operation}")
    print(f"Numbers: {a} and {b}")
    print(f"Result: {result}")

    input("\nPress Enter to continue...")
