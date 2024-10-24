# Define the functions for basic operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:  # Check for division by zero
        return "Error! Division by zero."
    else:
        return x / y


# Main loop of the calculator
def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the user input is valid (1, 2, 3, or 4)
        if choice in ['1', '2', '3', '4']:
            try:
                # Ask the user for two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform the operation based on user choice
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid choice! Please select a valid operation.")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break


# Run the calculator function
calculator()
