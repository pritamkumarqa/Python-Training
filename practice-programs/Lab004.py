def sqr(x):
    return x**2
list1=[1,2,3,4]
sq_numbers=map(sqr,list1)
print(sq_numbers)
print(type(sq_numbers))
list2=list(sq_numbers)
print(list2)

tot = sum(list1)
print(tot)
list4=[3.56773,5.57668,4.00944]
result=list(map(round,list4,range(1,4)))
print(result)

scores=[66,90,50,80,70,95,82]
def is_merit(mark):
    return mark > 75
merit_list=list(filter(is_merit,scores))
print(merit_list)


# Python 3
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)