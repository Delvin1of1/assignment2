#defining functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error wai!"
    return a / b

#defining the calculator (main)
def calculator():
    num1 = float(input("type in a number: "))
    num2 = float(input("type in another number: "))

    operation = input("select your operation(add, subtract, multiply, divide): ").lower()

#calculation
    if operation == "add":
        result = add(num1, num2)

    elif operation == "subtract":
        result = subtract(num1, num2)

    elif operation == "multiply":
        result = multiply(num1, num2)

    elif operation == "divide":
        result = divide(num1, num2)

    else:
        result = "Error wai"

#printing the result
    print(f"Result: {result}")

#calling main
calculator()



