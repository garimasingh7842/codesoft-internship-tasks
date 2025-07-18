def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations: 1.Add(+),  2.Subtract(-),  3.multiply(x),   4.divide(/)")

    try:
        num1 = float(input("Enter the first number: "))
       
        num2 = float(input("Enter the second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print(" Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print(" Invalid operation.")
            return

        print(f" Result: {num1} {op} {num2} = {result}")
    
    except ValueError:
        print(" Invalid input. Please enter numeric values.")

# Run calculator
calculator()
