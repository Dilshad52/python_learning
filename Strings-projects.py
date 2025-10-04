# Project 1: Word Counter

text = input("Enter a sentence: ")
words = text.split()
print("Word count:", len(words))
--------------------------------------------------------------------------------------------

#Project 2: Palindrome Checker

text = input("Enter a word: ")
if text == text[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome.")

