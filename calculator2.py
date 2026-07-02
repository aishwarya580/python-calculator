print("=== Simple Calculator ===")
print("Operations: +(add), -(subtract), *(multiply), /(division)")
print("Type 'exit' to quit")

while True:
    # Get the first number
    user_input1 = input("Enter first number (or exit to quit): ").strip()
    if user_input1.lower() == "exit":
        break

    try:
        num1 = float(user_input1)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    # Get the operation
    operation = input("Enter operation (+, -, *, /): ").strip()
    if operation.lower() == "exit":
        break

    # Get the second number
    user_input2 = input("Enter second number (or exit to quit): ").strip()
    if user_input2.lower() == "exit":
        break

    try:
        num2 = float(user_input2)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
    else:
        print("Invalid operation! Please enter +, -, *, or /.")
        continue

    # Display the result
    print(f"Result: {num1} {operation} {num2} = {result}")

print("Calculator closed.")