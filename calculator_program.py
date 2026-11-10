# Calculator Program

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Sum:", first_number + second_number)
print("Difference:", first_number - second_number)
print("Product:", first_number * second_number)

if second_number == 0:
    print("Division: Cannot divide by zero")
else:
    print("Division:", first_number / second_number)
