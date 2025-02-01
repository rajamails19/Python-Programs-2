def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word: ")
print(f"{word} is a palindrome" if is_palindrome(word) else f"{word} is not a palindrome")
