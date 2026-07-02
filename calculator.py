print("=== Simple Python Calculator ===")
print("Operations: + (add), - (subtract), * (multiply), / (divide)")
print("Type 'exit' to quit.\n")

while True:

    # 1. Get the first number
    user_input1 = input("Enter first number (or 'exit'): ").strip()
    if user_input1.lower() == 'exit':
        break
    num1 = float(user_input1)

    # 2. Get the operator
    operator = input("Enter operator (+, -, *, /): ").strip()
    if operator.lower() == 'exit':
        break

    # 3. Get the second number
    user_input2 = input("Enter second number: ").strip()
    if user_input2.lower() == 'exit':
        break
    num2 = float(user_input2)

    # 4. Perform the calculation based on the operator
    if operator == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}\n")

    elif operator == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}\n")

    elif operator == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}\n")

    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.\n")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}\n")

    else:
        print("Invalid operation selected. Please use one of the following: +, -, *, /\n")
        continue

print("Thank you for using the calculator. Goodbye!")