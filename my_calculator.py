#This is a simple script to simulate a simple calculator based on user input.

#Build four functions to represent the four basic operations:

#Addition
def add(x, y):
    return x + y

#Subtraction
def subtract(x, y):
    return x - y

#Multiplication
def multiply(x, y):
    return x * y

#Division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

#Get user input
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#Gather which operation the user wants to use.
choice = input("Enter choice (1/2/3/4): ")

#Gather the numbers the user wants to operate with.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Based on user input, operate.
if choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input")
