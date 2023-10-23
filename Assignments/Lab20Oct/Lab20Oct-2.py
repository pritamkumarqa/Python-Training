word1="naman"

def check_palindrome(str1):
    str2 = str1[-1::-1]    #Or you can use str1[::-1]
    if str1 == str2:
        print(f"String {str1} is palindrome")
    else:
        print(f"String {str1} is not palindrome")

check_palindrome(word1)

