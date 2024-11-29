#Calculator = Addition, Subtraction, Multiplication, Division and Power.
#Endless calculator.
#Enter random numbers in forst two inputs and 'q' in the third input to quit.

#defining the mathematical operations as functions
#addition
def add(x, y):
    return x + y

#subtraction
def subtract(x, y):
    return x - y

#multiplication
def multiply(x, y):
    return x * y

#division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

#power (bonus question)
def power(x, y):
    return x ** y

#defining the calculator as a function using the above (mathematical operations/) functions
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Enter '+' for addition, '-' for Subtraction, '*' for Multiplication, '/' for Division, '^' for Power")
            operation = input("Enter operation (+, -, *, /, ^ for power) or 'q' to quit: ")

            if operation == '+':
                print(f"The result is: {add(num1, num2)}")
            elif operation == '-':
                print(f"The result is: {subtract(num1, num2)}")
            elif operation == '*':
                print(f"The result is: {multiply(num1, num2)}")
            elif operation == '/':
                print(f"The result is: {divide(num1, num2)}")
            elif operation == '^':
                print(f"The result is: {power(num1, num2)}")
            # for continuous calculation or endless calculation
            elif operation.lower() == 'q':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Error: Invalid operation.")
        #if the value entered is of other type:
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()