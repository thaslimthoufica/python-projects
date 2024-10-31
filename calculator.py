def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Error: Division by zero"

# Dictionary for operation functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print("Simple Calculator")
    
    # Initial input
    num1 = float(input("Enter the first number: "))
    
    # Continuous calculation loop
    while True:
        # Display operations
        print("\nChoose an operation:")
        for symbol in operations:
            print(symbol)
        
        # User selects operation and enters next number
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        
        # Perform calculation
        if operation_symbol in operations:
            result = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        else:
            print("Invalid operation selected.")
            continue
        
        # Ask user if they want to continue with the result or start over
        choice = input("Type 'y' to continue calculating with this result, 'n' to start a new calculation, or 'exit' to quit: ")
        
        if choice == "y":
            num1 = result  # Continue with the current result
        elif choice == "n":
            calculator()  # Restart the calculator from scratch
            break
        elif choice == "exit":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Exiting.")
            break

calculator()

