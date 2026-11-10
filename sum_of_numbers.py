# Sum of Numbers Program
# This program adds a given number of user-entered values.

count = int(input("How many numbers do you want to add? "))
total = 0

# Repeat for each value the user wants to add
for i in range(1, count + 1):
    number = float(input(f"Enter number {i}: "))
    total += number

print("Total Sum:", total)
