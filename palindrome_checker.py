# Palindrome Checker
# This program checks whether a word or sentence reads the same backward.

text = input("Enter a word or sentence: ").lower().replace(" ", "")

# Compare the text with its reverse
if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
