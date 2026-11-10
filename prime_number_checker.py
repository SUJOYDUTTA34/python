# Prime Number Checker
# This program checks whether a number is prime.

number = int(input("Enter a number: "))

# Numbers less than or equal to 1 are not prime
if number <= 1:
    print(f"{number} is not a Prime Number")
else:
    is_prime = True
    # Check divisibility up to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is not a Prime Number")
