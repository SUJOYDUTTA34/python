# Sum of Numbers Program

count = int(input("How many numbers do you want to add? "))
total = 0

for i in range(1, count + 1):
    number = float(input(f"Enter number {i}: "))
    total += number

print("Total Sum:", total)
