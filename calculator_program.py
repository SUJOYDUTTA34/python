# Calculator Program
# This program takes two numbers and performs basic arithmetic operations.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Add the numbers
print("Sum:", first_number + second_number)
# Subtract the second number from the first number
print("Difference:", first_number - second_number)
# Multiply the numbers
print("Product:", first_number * second_number)

# Divide only if the second number is not zero
if second_number == 0:
    print("Division: Cannot divide by zero")
else:
    print("Division:", first_number / second_number)
