
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":

        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator"


print("Welcome to Simple Calculator!")
print("Available operations: +, -, *, /")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"Result: {result}")