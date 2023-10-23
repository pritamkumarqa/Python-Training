word1 = "naman"


def check_palindrome(str1):
    rev_word = ''
    for x in str1:
        rev_word = x + rev_word
    if word1 == rev_word:
        print(f"string {word1} is palindrome")
    else:
        print(f"string {word1} is not a palindrome")


check_palindrome(word1)
