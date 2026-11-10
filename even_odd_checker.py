# Even or Odd Checker
# This program checks whether a number is even or odd.

number = int(input("Enter a number: "))

# If the number is divisible by 2, it is even
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
