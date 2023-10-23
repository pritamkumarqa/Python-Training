'''
Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
Example - pramod  --> not a palindrome
madam - reverse(madam) -> same --> palindrome
'''
str1 = "maadaam"
def check_palindrome(a):
    list1 = list(a)
    print(list1)
    list2 = list1.copy()
    list2.reverse()
    print(list2)
    if list1 == list2:
        print(f"string {a} is palindrome")
    else:
        print(f"string {a} is not palindrome")

check_palindrome(str1)
