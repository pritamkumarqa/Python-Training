#Write a program to calculate the sum of digits of integer number. For eg: sum of 234 = 9
x=7123
list1 = list(str(x))
print(list1)
list2 = []
for y in list1:
    list2.append(int(y))
print(list2)
sum=0
for y in list2:
    sum = sum +y
print(f"final sum is {sum}")

