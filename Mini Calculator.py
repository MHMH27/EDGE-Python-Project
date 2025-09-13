#making a mini/basic calculator
# Calculator Functions

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):    # division (avoid zero)
    return x / y if y != 0 else "Error!!!!!!!!!!!!!!!! 00000000"
def floor_divide(x, y):
    return x // y if y != 0 else "Error!!!!!!!!!!! 000000000000"
def modulus(x, y):
    # remainder after division
    return x % y if y != 0 else "Error! Divided by 0!!."
def power(x, y):
    # x raised to the power y
    return x ** y
def percentage(x, y):
    # x percent of y
    return (x / 100) * y

print("MHMH Mini Calculator ")
print("_" * 27)

# The biG Menu
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Division")
print("6. Modulus")
print("7. Power")
print("8. Percentage")

choice = input("Enter choice (1-8): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform calculation based on user inputs
if choice == "1":
    print(f"Result: {add(a, b)}")
elif choice == "2":
    print(f"Result: {subtract(a, b)}")
elif choice == "3":
    print(f"Result: {multiply(a, b)}")
elif choice == "4":
    print(f"Result: {divide(a, b)}")
elif choice == "5":
    print(f"Result: {floor_divide(a, b)}")
elif choice == "6":
    print(f"Result: {modulus(a, b)}")
elif choice == "7":
    print(f"Result: {power(a, b)}")
elif choice == "8":
    print(f"Result: {percentage(a, b)}")
else:
    print("You made the wrong  choice FOOOOL")
