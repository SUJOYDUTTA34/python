# Multiplication Table Program
# This program prints the multiplication table of a number from 1 to 10.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
