# define the function for addition
def add(x, y):
    return x + y

# define the function for subtraction
def subtract(x, y):
    return x - y

# define the function for multiplication
def multiply(x, y):
    return x * y

# define the function for division
def divide(x, y):
    return x / y

# get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# display the menu of operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# get the user's choice of operation
choice = input("Enter choice (1/2/3/4): ")

# perform the selected operation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")