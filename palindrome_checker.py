# Palindrome Checker

text = input("Enter a word or sentence: ").lower().replace(" ", "")

if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
